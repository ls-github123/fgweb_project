from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from coupon.services import get_user_coupon_list
from coupon.services import get_user_coupon_list, get_user_enable_coupon_list
from fgweb_project_api.settings.utils import constants

# 获取优惠券列表
class CouponListView(APIView):
    permission_classes = [IsAuthenticated] # 配置访问权限 仅允许已认证用户访问
    
    def get(self, request):
        user_id = request.user.id
        # 工具类
        # coupon_list = get_user_coupon_list(user_id)
        coupon_list = get_user_coupon_list(1)
        return Response({"message":"优惠券列表获取成功", "coupon":coupon_list})
    
class EnableCouponListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # data = get_user_enable_coupon_list(request.user.id)
        data = get_user_enable_coupon_list(1)
        print(request.user.credit)
        print(data)
        return Response({"message":"可用优惠券列表返回成功",
                         "has_credit":request.user.credit,
                         "credit_to_money":constants.CREDIT_TO_MONEY,
                         "coupon_list":data
                         })
# 优惠券（获取优惠券列表，获取可用优惠券）、订单、订单的后端逻辑：视图、模型类、序列化器（业务逻辑的处理）
#     优惠券列表
#       用户可用积分
#         积分兑换比例