from django.contrib import admin
from course.models import CourseDirectionModel,CourseCategoryModel,CourseModel,TeacherModel
# Register your models here.

# 自定义django管理站点admin
class CoureDirectionModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseDirectionModel,CoureDirectionModelAdmin)

class CoureCategroyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseCategoryModel,CoureCategroyModelAdmin)

class CoureModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseModel,CoureModelAdmin)

class TeacherModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherModel,TeacherModelAdmin)