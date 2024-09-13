from django.urls import path,re_path
from course.views import IndexViews, CourseDirectionListApiView,CourseCategoryListApiView,\
    CourseListApiView, CourseDetaileViews, CourseChapterListApiView, CourseSearchViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register('search',CourseSearchViewSet,basename="course_search")

urlpatterns = [
    path('index/',IndexViews.as_view()),
    path('diretion/',CourseDirectionListApiView.as_view()),
    re_path(r'course/(?P<directionID>\d+)/(?P<categoryID>\d+)/$',CourseListApiView.as_view()),
    re_path(r'coursdetail/(?P<courseID>\d+)/$', CourseDetaileViews.as_view()),
    re_path(r'(?P<courseID>\d+)/chapters/$', CourseChapterListApiView.as_view()),
    # 重写
    # path('category/',CourseCategoryListApiView.as_view()),
    re_path(r'^category/(?P<directionID>\d+)/$',CourseCategoryListApiView.as_view()),
]

urlpatterns += router.urls