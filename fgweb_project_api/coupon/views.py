from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from coupon.services import get_user_coupon_list
from coupon.services import get_user_coupon_list, get_user_enable_coupon_list

# 获取优惠券列表
class CouponListView(APIView):
    permission_classes = [IsAuthenticated] # 配置访问权限 仅允许已认证用户访问
    
    def get(self, request):
        user_id = request.user.id
        # 工具类
        # coupon_list = get_user_coupon_list(user_id)
        coupon_list = get_user_coupon_list(1)
        return Response({"message":"优惠券列表获取成功", "coupon":coupon_list})