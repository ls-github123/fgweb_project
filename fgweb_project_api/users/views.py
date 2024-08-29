from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UsersModel
from rest_framework import status
from rest_framework.generics import CreateAPIView
from users.userserializer import RegisterSerializer

class UsersTestViews(APIView):
    # 临时测试用户注册功能
    def post(self, request):
        user = UsersModel.objects.create_user("zhangsan","lps443@outlook.com", "123456", mobile="18012345678")
        return Response({"message":"注册成功"})
    
# 手机号唯一性判断模块
class MobileApiView(APIView):
    def get(self, request, mobile):
        try:
            UsersModel.objects.get(mobile__exact=mobile)
            return Response({"message":"当前手机号已存在,请直接登录或更换手机号"}, status=status.HTTP_400_BAD_REQUEST)
        except UsersModel.DoesNotExist:
            return Response({"message":"当前手机号未注册"}, status=status.HTTP_200_OK)
        
# 用户注册视图模块
class RegisterViews(CreateAPIView):
    queryset = UsersModel.objects.all()
    # 校验、create\update
    serializer_class = RegisterSerializer