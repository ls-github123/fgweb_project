from django.urls import path
from home.views import NavViews

urlpatterns = [
    path('nav/', NavViews.as_view()),
]
