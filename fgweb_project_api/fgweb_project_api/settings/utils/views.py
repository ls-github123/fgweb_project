from . import constants
from rest_framework.generics import ListAPIView
# 装饰基于类的视图的每个实例
from django.utils.decorators import method_decorator
# 视图缓存
from django.views.decorators.cache import cache_page

class CacheListApiView(ListAPIView):
    @method_decorator(cache_page(60*10)) # 将函数装饰器转为类方法装饰器
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)