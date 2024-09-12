from django.urls import path
from pays.views import IndexViews, AliPayViewSet
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register('alipay', AliPayViewSet, basename='alipay')

urlpatterns = [
    path('testpay/', IndexViews.as_view()),
]
urlpatterns += router.urls