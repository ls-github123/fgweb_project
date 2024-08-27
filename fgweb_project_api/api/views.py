from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django_redis import get_redis_connection # redis数据库连接包

# 
def index(request):
    a = 10/0
    return HttpResponse('返回数据')

class IndexViews(APIView):
    def get(self, request):
        redis_con = get_redis_connection('default')
        name = redis_con.get('name')
        print(name)
        return HttpResponse('API返回数据')