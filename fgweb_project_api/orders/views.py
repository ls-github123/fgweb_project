from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from orders.models import OrdersModel
from orders.ser import OrderModelSerializer

class OrderCreateApiViews(CreateAPIView):
    permission_classes = [IsAuthenticated] # 配置访问权限 仅允许已认证用户访问
    queryset = OrdersModel.objects.all()
    serializer_class = OrderModelSerializer