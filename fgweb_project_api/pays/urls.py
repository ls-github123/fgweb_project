from django.urls import path
from pays.views import IndexViews

urlpatterns = [
    path('testpay/',IndexViews.as_view()),
]