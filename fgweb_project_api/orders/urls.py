from django.urls import path
from orders.views import OrderCreateApiViews

urlpatterns = [
    path('orders/',OrderCreateApiViews.as_view()),
]
