from django.urls import path, re_path
from users.views import UsersTestViews, RegisterViews, MobileApiView
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
from users.views_sms import SMSApiViews
urlpatterns = [
    # 临时测试用户注册功能
    path('registers_test/', UsersTestViews.as_view()),
    
    path('jwt/access/',TokenObtainPairView.as_view()),
    path('jwt/refresh/',TokenRefreshView.as_view()),
    path('jwt/verify/',TokenVerifyView.as_view()),
    
    # 正式注册
    path('register/', RegisterViews.as_view()),
    
    # 手机号注册校验接口
    re_path(r'^mobile/(?P<mobile>1[3-9]\d{9})/$', MobileApiView.as_view()),
    
    # 验证码发送接口
    re_path(r'^sendsms/(?P<mobile>1[3-9]\d{9})/$', SMSApiViews.as_view()),
]
