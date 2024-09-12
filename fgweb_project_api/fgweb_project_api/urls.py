"""
URL configuration for fgweb_project_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('home/', include('home.urls')),
    path('users/', include('users.urls')),
    path('course/', include('course.urls')),
    path('cart/', include('cart.urls')),
    path('coupon/', include('coupon.urls')),
    path('order/', include('orders.urls')),
    path('pay/', include('pays.urls')), # 支付宝接口调用
    path('ckeditor/', include('ckeditor_uploader.urls')), # 富文本编辑器路径
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)