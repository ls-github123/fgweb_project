from django.urls import path
from home.views import NavHeaderListViews, NavFooterListViews

urlpatterns = [
    path('headnav/', NavHeaderListViews.as_view()),
    path('footernav/', NavFooterListViews.as_view()),
]
