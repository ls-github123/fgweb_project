from django.urls import path,re_path
from course.views import IndexViews

urlpatterns = [
    path('index/',IndexViews.as_view()),
]