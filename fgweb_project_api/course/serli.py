from rest_framework import serializers
from course.models import CourseDirectionModel, CourseCategoryModel, CourseModel, TeacherModel

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