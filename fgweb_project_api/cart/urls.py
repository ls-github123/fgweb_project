from django.urls import path,re_path
from cart.views import CartViews, CartToOrderViews

urlpatterns = [
    path('cart/',CartViews.as_view()),
    path('cartorder/', CartToOrderViews.as_view()),
]