from django.urls import path
from coupon.views import CouponListView, EnableCouponListView

urlpatterns = [
    path('list/', CouponListView.as_view()),
    path('enable/', EnableCouponListView.as_view()),
]