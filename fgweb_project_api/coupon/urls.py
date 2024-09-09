from django.urls import path
from coupon.views import CouponListView

urlpatterns = [
    path('list/', CouponListView.as_view()),
]