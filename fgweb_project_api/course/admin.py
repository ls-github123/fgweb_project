from django.contrib import admin
from course.models import CourseDirectionModel,CourseCategoryModel,CourseModel,TeacherModel
# Register your models here.

# 自定义django管理站点admin

# StackedInline:让外键对应的数据垂直排列(表单格式)
# Tabularzinline:让外键对应的数据横向排列(表格的一行)
class CoreseCategoryInLine(admin.StackedInline):
    model = CourseCategoryModel
    fields = ['id', 'name', 'orders']

# 方向列表
class CoureDirectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'recomment_home_hot', 'recomment_home_top']
    ordering = ['id']
    list_filter = ['recomment_home_hot', 'recomment_home_top']
    search_fields = ['id', 'name']
    inlines = [CoreseCategoryInLine,]
admin.site.register(CourseDirectionModel,CoureDirectionModelAdmin)

# 课程分类
class CoureCategroyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'remark', 'direction']
admin.site.register(CourseCategoryModel,CoureCategroyModelAdmin)

# 课程信息
class CoureModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'students', 'pub_date', 'status']
admin.site.register(CourseModel,CoureModelAdmin)

# 讲师信息
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'avatar_small', 'name','role', 'title', 'signature']
    ordering = ['id']
admin.site.register(TeacherModel,TeacherModelAdmin)