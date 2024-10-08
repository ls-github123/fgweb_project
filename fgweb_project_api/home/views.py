from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import NavSerializer, BannerSerializer
from rest_framework.generics import ListAPIView
from home.models import NavModel, BannerModel
from fgweb_project_api.settings.utils import constants
from fgweb_project_api.settings.utils.views import CacheListApiView # 继承首页视图缓存方法

class NavHeaderListViews(CacheListApiView):
    queryset = NavModel.objects.filter(is_show=True,is_deleted=False,postion=constants.NAV_HEARD).order_by('-id')[:constants.NAV_HEARD_SIZE]
    serializer_class = NavSerializer
    
class NavFooterListViews(CacheListApiView):
    queryset = NavModel.objects.filter(is_show=True,is_deleted=False,postion=constants.NAV_FOOTER).order_by('-id')[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavSerializer
    
class BannerListView(CacheListApiView):
    queryset = BannerModel.objects.filter(is_show=True,is_deleted=False).order_by('-id')[:constants.BANNER_SIZE]
    serializer_class = BannerSerializer