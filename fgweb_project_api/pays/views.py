from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from fgweb_project_api.settings.utils.alipaysdk import AliPaySDK
# Create your views here.


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