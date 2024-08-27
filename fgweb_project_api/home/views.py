from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import NavSerializer
from home.models import NavModel

class NavViews(APIView):
    def get(self, request):
        # 测试,暂时查询所有数据
        navmodel = NavModel.objects.filter(is_show=True, is_deleted=False, postion=0)
        navser = NavSerializer(instance = navmodel, many=True)
        return Response({"message":"导航菜单请求", "data":navser.data})