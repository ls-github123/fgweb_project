from rest_framework import serializers
from orders.models import OrdersModel,OrderDetaileModel
from django_redis import get_redis_connection
from django.db import transaction
from course.models import CourseModel
from coupon.models import CouponModels,CouponLogModel
from fgweb_project_api.settings.utils import constants
import datetime


class OrderModelSerializer(serializers.ModelSerializer):
    user_coupon_id = serializers.IntegerField(write_only=True,default=None)
    class Meta():
        model = OrdersModel
        fields = ['id','pay_type','credit','user_coupon_id']
        extra_kwargs = {
            "pay_type":{"write_only":True},
            "credit":{"write_only":True}
        }
    def create(self, validated_data):
        # 往订单表中添加新订单
        # 用户
        user = self.context['request'].user
        user_id = user.id
        # 课程
        # 根据用户获取购物车中所选择得商品（课程）
        redis = get_redis_connection('cart')
        cart_hash = redis.hgetall(f"cart_{user_id}")

        if len(cart_hash)<1:
            raise serializers.ValidationError(detail="购物车中没有商品",code='cart_empty')

        # 积分---获取本次下单用户选择兑换得积分
        use_credit = int(validated_data.get('credit',0))

        if use_credit > 0 and use_credit>user.credit:
            raise serializers.ValidationError(detail="您的积分本次不够划扣", code='credit_error')

        # 优惠券
        user_coupon_id = validated_data.get('user_coupon_id',None)
        user_coupon1 = None

        if user_coupon_id is not None:
            user_coupon1 = CouponLogModel.objects.filter(id=user_coupon_id,user_id=user_id).first()

        # 创建订单操作订单，开启数据库事务
        with transaction.atomic():
            # 创建事务得还原点
            t1 = transaction.savepoint()
            # 创建订单
            try:

                orders = OrdersModel.objects.create(
                    name="浮光商城课程购买订单",
                    user_id=user_id,
                    # 基于redis生成分布式得唯一订单号
                    order_number=datetime.datetime.now().strftime('%Y%m%d')+("%08d" % user_id) + "%08d" % redis.incr('order_number'),
                    pay_type=validated_data.get('pay_type'),
                )

                # 订单记录表创建完成，获取课程列表，生成订单详情数据，并外键添加
                # 在获取到课程列表情况下，通过循环课程列表，计算：所有课程可用积分
                # 最优优惠券，
                # 订单总价 、  优惠活动得优惠价格
                # 课程总价
                course_id_list = [int(key.decode()) for key,value in cart_hash.items() if value == b'1']
                # 根据选中购物车列表中得id结果集，获取数据库中对应课程列表
                course_list = CourseModel.objects.filter(id__in=course_id_list,is_deleted=False,is_show=True)
                # 订单总价
                total_price = 0  #本次下单总价
                real_price = 0  # 优惠活动得价格，循环计算所有课程

                max_discount_course = None # 最优课程

                # 积分--计算最多可以抵扣积分
                max_use_credit = 0

                total_discount_price = 0  # 最终折扣价格
                # 循环
                detail_list = []
                for course in course_list:
                    discount_price = course.discount.get('price',course.price)
                    discount_name = course.discount.get('type',"")

                    # 循环创建订单详情
                    detail_list.append(OrderDetaileModel(
                        order=orders,
                        course=course,
                        price=course.price,
                        real_price=discount_price,
                        discount_name=discount_name,
                    ))
                    # 计算总价
                    total_price += float(course.price)
                    # 计算优惠价格
                    real_price += float(discount_price)
                    # 找到最优课程，优惠券
                    if user_coupon1:
                        if max_discount_course is None:
                            max_discount_course = course
                        else:
                            # 循环判断当前课程得价格，是否大于已经存在得最优惠课程得价格
                            if course.price >= max_discount_course.price:
                                max_discount_course = course

                     #表示用户选用积分          表示课程允许用积分抵扣
                    if use_credit > 0 and course.credit > 0:
                        # 循环课程，获取最大可以使用积分
                        max_use_credit += course.credit
                # 一次性往数据库添加商品详情列表对象
                OrderDetaileModel.objects.bulk_create(detail_list)

                # 计算最终优惠价格
                # 优惠券   或者是   积分
                if user_coupon1:
                    # 拿到优惠券   优惠公式    -100    0.82
                    sale = user_coupon1.coupon.sale[1:]
                    if user_coupon1.coupon.discount == 1:
                        # 减免优惠券
                        total_discount_price = float(sale)
                    elif user_coupon1.coupon.discount == 2:
                        total_discount_price = float(float(max_discount_course.price)*(1-float(sale)))

                # 积分
                if use_credit > 0:
                    if max_use_credit < use_credit:
                        raise serializers.ValidationError(detail="超过当前最大可用积分限制",code='credit_max')

                    # 给订单记录表赋值
                    orders.credit = use_credit
                    # 把积分换成钱
                    total_discount_price = float(use_credit/constants.CREDIT_TO_MONEY)
                    # 扣除用户得最终积分
                    user.credit = user.credit - use_credit

                # 给订单列表赋值，课程总价    实际付款金额
                orders.total_price = total_price
                orders.real_price = float(real_price) - float(total_discount_price)

                orders.save()

                # 删除购物车中得数据
                # cart =
                cart = {key:value for key,value in cart_hash.items() if value == b'0'}

                # 删除redis中购物车所有关于当前用户得数据

                pipe = redis.pipeline()
                pipe.multi()
                pipe.delete(f"cart_{user_id}")
                if len(cart)>0:
                    pipe.hset(f'cart_{user_id}',mapping=cart)
                pipe.execute()

                # 优惠券id，直接获取优惠券对象，获取优惠券日志管理类对象
                if user_coupon1:
                    # 将优惠券 绑定到订单中
                    user_coupon1.order = orders
                    redis = get_redis_connection('coupon')
                    redis.delete(f'{user_id}:{user_coupon_id}')

                # 返回订单对象
                return orders
            except Exception as es:
                print('订单生成失败....')
                print(es)
                transaction.savepoint_rollback(t1)
                raise serializers.ValidationError(detail='订单生成失败,请稍后再试...',code='order_error')