from rest_framework import serializers
from course.models import CourseDirectionModel, CourseCategoryModel, CourseModel, TeacherModel, CourseChapterModel
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import CourseIndex
from django.conf import settings

class CourseDirectionSerializers(serializers.ModelSerializer):
    class Meta():
        model = CourseDirectionModel
        fields = ['id','name']

class CourseCategorySerializers(serializers.ModelSerializer):
    class Meta():
        model = CourseCategoryModel
        fields = ['id','name']
        
class CourseSerializers(serializers.ModelSerializer):
    class Meta():
        model = CourseModel
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta():
        model = TeacherModel
        fields = ['id', 'get_role_display', 'title', 'signature', 'avatar', 'brief']
        
class CourseRetrieveSerializer(serializers.ModelSerializer):
    direction_name = serializers.CharField(source='direction.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    # 嵌套序列化
    teacher = TeacherSerializer()
    
    class Meta():
        model = CourseModel
        # 声明返回数据
        fields = ['name','course_cover','course_video','course_type','get_level_display',
                  'description','status','pub_date','period','attachment_path',
                  'attachment_link','students','lessons','pub_lessons','price',
                  'credit','direction_name','category_name','direction','category','teacher','discount']
        
class CourseChapterSerializer(serializers.ModelSerializer):
    get_lesson_list = serializers.SerializerMethodField()
    
    class Meta():
        model = CourseChapterModel
        fields = ['id','orders','name','summary','pub_date','course','get_lesson_list']
        
    # def get_lesson_list(self, obj):
    #     return obj.get_lesson_list()  # 确保调用模型中的方法

    
class  CourseIndexHaystackSerializer(HaystackSerializer):
    """课程搜索的序列化器"""
    class Meta:
        index_classes = [CourseIndex]
        fields = ["text", "id", "name", "course_cover", "get_level_display", "students", "get_status_display", "pub_lessons", "price", "discount", "orders"]

    def to_representation(self, instance):
        """用于指定返回数据的字段的"""
        # 课程的图片，在这里通过elasticsearch提供的，所以不会提供图片地址左边的域名的。因此在这里手动拼接
        # instance.course_cover = f'//{settings.OSS_BUCKET_NAME}.{settings.OSS_ENDPOINT}/uploads/{instance.course_cover}'
        instance.course_cover = f"http://127.0.0.1:8000/uploads/{instance.course_cover}"
        return super().to_representation(instance)   