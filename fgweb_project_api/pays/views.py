from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from fgweb_project_api.settings.utils.alipaysdk import AliPaySDK
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from orders.models import OrdersModel
from coupon.models import CouponLogModel
from course.serli import CourseRetrieveSerializer
from course.models import CourseModel
from rest_framework import status

# 测试 获取支付连接，
# 给前端返回支付连接，前端支付
class IndexViews(APIView):
    def get(self,request):
        alipay = AliPaySDK()

        link = alipay.page_pay("2024091210520091345",'0.01','测试购买一个小米手机')
        print('-----------支付连接开始-------------')
        print(link)
        print('-----------支付连接结束-------------')

        return Response({'message':'车工'})


# 视图集路由配置方式
# AliPayViewSet.as_view({"get":"list","post":"create","get":"link"})
class AliPayViewSet(ViewSet):
    @action(methods=['GET'],detail=False)
    def link(self,request):
        order_id = request.query_params.get('order_id')
        print('获取订单id...')
        print(order_id)
        # 根据订单id查询订单详情
        try:
            order = OrdersModel.objects.get(pk=order_id)
            if order.order_status > 0:
                return Response({"message": "订单不能重复支付或者订单已经超时..."}, status=status.HTTP_404_NOT_FOUND)
        except OrdersModel.DoesNotExist:
            print('订单不存在,响应异常信息...')
            return Response({"message": "订单不存在，请重新下单..."},status=status.HTTP_404_NOT_FOUND)

        alipay = AliPaySDK()
        link = alipay.page_pay(order.order_number,order.real_price,order.name)
        print('----------打印支付链接开始--------------------')
        print(link)
        print('----------打印支付链接结束--------------------')
        return Response(link)
        # 测试
    @action(methods=['GET'],detail=False)
    def return_result(self,request):
        # 接收支付宝同步返回得支付结果，并处理
        data = request.query_params.dict()
        # 校验数据
        alipay = AliPaySDK()
        success = alipay.check_sign(data)
        if not success:
            return Response({"message": "支付宝同步通知结果不存在或者错误..."},status=status.HTTP_400_BAD_REQUEST)
        # 查询参数，获取同步通知中得订单号
        order_number = data.get('out_trade_no')

        # 根据订单号，查询订单，并修改订单状态
        try:
            order = OrdersModel.objects.get(order_number=order_number)
            if order.order_status > 1:
                return Response({"message": "当前订单已取消或者超时..."},status=status.HTTP_400_BAD_REQUEST)
        except OrdersModel.DoesNotExist:
            return Response({"message": "订单不存在...."},status=status.HTTP_400_BAD_REQUEST)

        # 如果当前订单没有问题，表示支付成功，
        # 将当前支付成功得信息和订单信息查询完成，给前端展示

        order_course = order.order_courses.all()
        # query_set 结果集
        # 通过详情列表，查询对应课程，并完成组装成一个课程列表
        course_list = [item.course for item in order_course]

        # 修改状态：订单状态   优惠券状态  ：使用时间  最终返回给前端展示

        # 判断当前订单状态时是否未0
        if order.order_status == 0:
            # 根据订单号再次查询支付结果
            result = alipay.query(order_number)
            print('打印再次查询支付结果.....')
            print(result)
            # 通过结果获取，支付宝给返回得订单支付状态
            # TRADE_SUCCESS 交易支付成功。  TRADE_FINISHED	交易结束，不可退款。
            if result.get('trade_status',None) in ['TRADE_SUCCESS','TRADE_FINISHED']:
                # 表示用户支付成功
                # 获取支付时间 -----  有待验证
                order.pay_time = result.get('send_pay_date')
                order.order_status = 1
                order.save()

                # 优惠券使用时间,根据订单，查询优惠日志管理对象，修改优惠券使用使劲啊
                coupon_log = CouponLogModel.objects.filter(order=order).first()
                # 如果优惠券存在
                if coupon_log :
                    # 需要验证，支付结果中得返回支付时间
                    coupon_log.use_time  = order.pay_time
                    # 修改优惠券使用状态
                    coupon_log.use_status = 1
                    coupon_log.save()

            # 将订单对应得外键关联课程，并序列化，用作返回展示
            coruse_ser = CourseRetrieveSerializer(instance=course_list,many=True)

            # 返回结果：
            #     支付时间
            #     支付价格
            #     商品列表（课程列表）
            return Response({
                "pay_time":order.pay_time,
                "real_price":order.real_price,
                "course_list":coruse_ser.data
            })