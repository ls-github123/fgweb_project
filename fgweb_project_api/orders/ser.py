 
from rest_framework import serializers
from orders.models import OrdersModel, OrderDetaileModel
from django_redis import get_redis_connection
from django.db import transaction
from course.models import CourseModel
from coupon.models import CouponModels
import datetime

class OrderModelSerializer(serializers.ModelSerializer):
    user_coupon_id = serializers.IntegerField(write_only=True, default=None)
    class Meta():
        # 订单超时
        fields = ['pay_type', 'id', 'user_coupon_id', 'credit']
        extra_kwargs = {
            "pay_type":{"write_only":True},
            "credit":{"write_only":True},
        }
    def create(self, validated_data):
        # 积分获取和判断
        # 优惠券获取和判断
        user = self.context['request'].user
        user_id = user.id
        
        # 购买课程 -- 获取购物车中课程
        redis = get_redis_connection('cart')
        # 获取当前用户课程列表
        cart_hash = redis.hgetall(f"cart_{user_id}")
        
        if len(cart_hash) < 1:
            raise serializers.ValidationError(detail="购物车没有数据", code="cart_enpty")
        
        # 获取前端传递的使用积分
        use_credit = validated_data.get('credit', 0)
        # 判断当前用户是否选择积分, 且积分是否足够划扣
        if use_credit > 0 and use_credit > user.credit:
            raise serializers.ValidationError(detail='您的积分不足,请重新选择', code='credir_error')
        
        # 开启数据库事务操作
        # 原子性 隔离性 一致性 持久性
        with transaction.atomic():
            # 创建一个还原点
            t1 = transaction.savepoint()
            try:
                # 创建订单 获取订单对象 并获取模型对象
                orders = OrdersModel.objects.create(
                    name = '浮光商城课程购买订单',
                    user_id = user_id,
                    # 生成自定义规则的订单号 --- 保证唯一性
                    order_number = datetime.datetime.now().strftime("%Y%m%d") + ("%08d" % user_id) + "%08d" % redis.incr("order_number"),
                    pay_type = validated_data.get('pay_type'),
                )
                # 获取购物车选中课程
                # 将课程从数据库中查询
                # 计算金额
                # 获取购物车中,选中的商品列表
                course_id_list = [int(key.decode()) for key,value in cart_hash.items() if value==b'1']
                # 从数据库中查询课程列表
                course_list = CourseModel.objects.filter(id__in=course_id_list,is_deleted=False,is_show=True)

                total_price = 0 # 本次所有商品/课程的总价
                real_price = 0 # 本次订单实付金额，优惠后的价格
                # 构建一个空列表，用于订单列表
                detail_list = []
                # 获取前端传递的优惠券id
                user_coupon_id = validated_data.get('user_coupon_id')
                user_coupon = None
                max_discount_course = None   # 计算最优优惠券--课程
                totol_discount_price = 0   # 总优惠价格
                # 如果前端传递了优惠券id，且不为空，获取优惠券信息
                if user_coupon_id is not None:
                    user_coupon = CouponModels.objects.filter(id=user_coupon_id,user_id=user_id).first()

                max_use_credit = 0  #本次下单，最多可以抵扣的积分

                # 循环课程，统计价格，优惠相关信息，生成订单】
                for course in course_list:
                    # 获取当前课程优惠价格，如果没有优惠价格，则赋值课程原价
                    discount_price = course.discount.get('price',course.price)
                    discount_name = course.discount.get('type',"")
                    # 创建订单详情表   --  没有执行save   没执行crete
                    detail_list.append(OrderDetaileModel(
                        order=orders,
                        course = course,
                        name = discount_name,
                        price=course.price,
                        real_price= discount_price,
                    ))
                    # 循环，计算课程的总价和实际付款价格
                    total_price += float(course.price)
                    # 循环，计算课程优惠价格
                    real_price += discount_price
                    # 判断   先获取
                    if user_coupon:
                        # 判断当前最优惠课程，是否有数据，没有默认赋值当前循环的课程
                        if max_discount_course is None:
                            max_discount_course = course
                        else:
                            # 判断当前循环的课程价格，是否大于已经存在的最优惠的课程的价格
                            #     价格越高，使用优惠更优惠
                            if course.price >= max_discount_course.price:
                                max_discount_course = course
                    # 积分  每个课程的积分，循环相加
                    if use_credit > 0 and course.credit >0:
                        max_use_credit +=course.credit
                # 往数据库中，添加订单详情列表数据
                OrderDetaileModel.objects.bulk_create(detail_list)

                # 优惠券操作
                # 积分计算
                # redis处理
                #  购物车、优惠券
            except Exception as es:
                print('订单创建失败...')
                print(es)
                transaction.savepoint_rollback(t1)
                raise serializers.ValidationError(detail='订单生成失败', code='order_error')