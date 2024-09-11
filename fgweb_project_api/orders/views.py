from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from orders.models import OrdersModel
from orders.ser import OrderModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.ser import OrderModelSerializer, OrderListModelSerializer
from rest_framework.pagination import PageNumberPagination

# 生成订单
class OrderCreateApiViews(CreateAPIView):
    permission_classes = [IsAuthenticated] # 配置访问权限 仅允许已认证用户访问
    queryset = OrdersModel.objects.all()
    serializer_class = OrderModelSerializer
    
# 获取订单状态列表   选项
class OrderPayStatusChoicesApiView(APIView):
    def get(self,request):
        return Response(OrdersModel.STATUS_CHOICES)

# 获取当前订单列表
# 分页

class OrdersListPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10

class OrderListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListModelSerializer
    pagination_class = OrdersListPageNumberPagination
    # queryset = OrdersModel.objects.all()
    def get_queryset(self):
        user = self.request.user
        # print(user)
        # 根据当前用户，查询全部订单
        query_set = OrdersModel.objects.filter(user=user, is_deleted=False, is_show=True)
        # print(query_set)
        order_status = int(self.request.query_params.get('status',-1))

        # 获取数据库存储得订单状态码
        status_list = [item[0] for item in OrdersModel.STATUS_CHOICES]

        if order_status in status_list:
            query_set = query_set.filter(order_status=order_status)

        return query_set.order_by('-id')