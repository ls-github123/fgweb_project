from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from course.models import TeacherModel, CourseDirectionModel, CourseCategoryModel, CourseModel, CourseChapterModel
from rest_framework.generics import ListAPIView, RetrieveAPIView
from course.serli import CourseDirectionSerializers,CourseCategorySerializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from course.serli import CourseDirectionSerializers,CourseCategorySerializers,CourseSerializers,CourseRetrieveSerializer,\
    CourseChapterSerializer, CourseIndexHaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.filters import OrderingFilter
from drf_haystack.filters import HaystackFilter


class CoursePageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = "size"
    max_page_size = 10

# ES搜索视图  课程信息全文检索视图
class CourseSearchViewSet(HaystackViewSet):
    # 指定本次搜索得最终真实数据得保存模型
    index_models = [CourseModel]
    serializer_class = CourseIndexHaystackSerializer
    filter_backends = [OrderingFilter,HaystackFilter]
    ordering_fields = ('id','students','orders')
    pagination_class = CoursePageNumberPagination

# 课程方向视图
class CourseDirectionListApiView(ListAPIView):
    queryset = CourseDirectionModel.objects.filter(is_show=True,is_deleted=False).order_by('id')
    serializer_class = CourseDirectionSerializers
    pagination_class = None

# 课程分类列表实现
class CourseCategoryListApiView(ListAPIView):
    # queryset = CourseCategoryModel.objects.filter(is_show=True,is_deleted=False).order_by('id')
    serializer_class = CourseCategorySerializers
    # 重写get_queryset方法，根据指定条件，自定义返回内容
    def get_queryset(self):
        # 获取参数 --- -查询数据
        print('-------查询课程分类-----------')
        print(self.kwargs)
        directionID = int(self.kwargs.get('directionID', 0))
        query_set = CourseModel.objects.filter(is_show=True, is_delete=False).order_by('id')
        if directionID > 0:
            # 获取到前端传递得方向ID
            query_set = query_set.filter(direction=directionID)
        
        return query_set

# 课程列表视图
class CourseListApiView(ListAPIView):
    serializer_class = CourseSerializers
    pagination_class = CoursePageNumberPagination
    filter_backends = [OrderingFilter] # 局部指定过滤器
    ordering_fields = ['id', 'price', 'students']
    
    def get_queryset(self):
        # 获取两个参数
        directionID = int(self.kwargs.get('directionID', 0))
        categoryID = int(self.kwargs.get('categoryID', 0))
        
        query_set = CourseModel.objects.filter(is_show=True, is_deleted=False).order_by('id')
        
        if directionID > 0:
            query_set = query_set.filter(direction=directionID)
        
        if categoryID > 0:
            query_set = query_set.filter(category=categoryID)
        
        return query_set

class CourseDetaileViews(RetrieveAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseRetrieveSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'courseID'

# 根据课程ID, 获取章节列表
class CourseChapterListApiView(ListAPIView):
    queryset = CourseChapterModel.objects.all()
    serializer_class = CourseChapterSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'courseID'


class IndexViews(APIView):
    """
    阿里云oss测试视图
    """
    def get(self,request):
        teas = TeacherModel.objects.all()

        for ta in teas:
            # print(ta.avatar.url)
            print(ta.avatar.thumb_50x50.url)

        return Response({"message":"老师列表","data":""})