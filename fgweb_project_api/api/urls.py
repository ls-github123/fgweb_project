from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('indexview/', views.IndexViews.as_view()),
]
