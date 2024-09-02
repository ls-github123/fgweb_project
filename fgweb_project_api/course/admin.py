from django.contrib import admin
from course.models import CourseDirectionModel,CourseCategoryModel,CourseModel,TeacherModel
# Register your models here.

admin.site.register(CourseDirectionModel)
admin.site.register(CourseCategoryModel)
admin.site.register(CourseModel)
admin.site.register(TeacherModel)