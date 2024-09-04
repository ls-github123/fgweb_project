from django.urls import path,re_path
from course.views import IndexViews,CourseDirectionListApiView,CourseCategoryListApiView,\
    CourseListApiView, CourseDetaileViews

urlpatterns = [
    path('index/',IndexViews.as_view()),
    path('diretion/',CourseDirectionListApiView.as_view()),
    re_path(r'course/(?P<directionID>\d+)/(?P<categoryID>\d+)/$',CourseListApiView.as_view()),
    re_path(r'detailes/(?P<courseID>\d+)/$', CourseDetaileViews.as_view()),
    # 重写
    # path('category/',CourseCategoryListApiView.as_view()),
    re_path(r'^category/(?P<directionID>\d+)/$',CourseCategoryListApiView.as_view()),
]