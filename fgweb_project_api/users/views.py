from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UsersModel

class UsersTestViews(APIView):
    def post(self, request):
        user = UsersModel.objects.create_user("admin","lpsserver443@outlook.com", "123")
        return Response({"message":"注册成功"})