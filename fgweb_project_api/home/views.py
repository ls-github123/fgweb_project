from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import NavSerializer
from rest_framework.generics import ListAPIView
from home.models import NavModel
from fgweb_project_api.settings.utils import constants

class NavHeaderListViews(ListAPIView):
    queryset = NavModel.objects.filter(is_show=True,is_deleted=False,postion=constants.NAV_HEARD).order_by('-id')[:constants.NAV_HEARD_SIZE]
    serializer_class = NavSerializer
    
class NavFooterListViews(ListAPIView):
    queryset = NavModel.objects.filter(is_show=True,is_deleted=False,postion=constants.NAV_FOOTER).order_by('-id')[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavSerializer