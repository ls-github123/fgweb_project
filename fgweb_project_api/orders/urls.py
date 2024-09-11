from django.urls import path
from orders.views import OrderCreateApiViews, OrderPayStatusChoicesApiView, OrderListApiView

urlpatterns = [
    path('orders/', OrderCreateApiViews.as_view()),
    path('chioces/',OrderPayStatusChoicesApiView.as_view()),
    path('list/',OrderListApiView.as_view())
]
