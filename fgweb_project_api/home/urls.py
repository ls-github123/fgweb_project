from django.urls import path
from home.views import NavHeaderListViews, NavFooterListViews, BannerListView

urlpatterns = [
    path('headnav/', NavHeaderListViews.as_view()),
    path('footernav/', NavFooterListViews.as_view()),
    path('banner/', BannerListView.as_view()),
]
