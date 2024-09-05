from django.urls import path,re_path
from cart.views import CartViews

urlpatterns = [
    path('cart/',CartViews.as_view()),
]