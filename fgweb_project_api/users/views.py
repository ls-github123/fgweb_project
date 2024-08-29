from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UsersModel

class UsersTestViews(APIView):
    def post(self, request):
        user = UsersModel.objects.create_user("zhangsan","lps443@outlook.com", "123456", mobile="18012345678")
        return Response({"message":"注册成功"})