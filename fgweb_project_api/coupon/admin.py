from typing import Any
from django.contrib import admin
from . import models
from django_redis import get_redis_connection
import json

# 课程专业/方向
# 外键关联类的管理站点内嵌显示
class CouponDiretionInLine(admin.TabularInline):
    model = models.CouponCourseDirectionModel
    fields = ['id', 'direction']
    
# 课程分类
# 外键关联类的管理站点内嵌显示
class CouponCategoryInLine(admin.TabularInline):
    model = models.CouponCourseCategoryModel
    fields = ['id', 'category']
    
# 课程信息
class CouponCourseInLine(admin.TabularInline):
    model = models.CouponCourseModel
    fields = ['id', 'coupon', 'course']
    
# 优惠券
class CouponModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_time', 'end_time',
                    'total', 'has_total', 'coupon_type', 'get_type']
    inlines = [CouponDiretionInLine, CouponCategoryInLine, CouponCourseInLine]
admin.site.register(models.CouponModels, CouponModelsAdmin)

# 日志/发送管理
class CouponLogModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'coupon', 'use_time', 'use_status']
    def save_model(self, request, obj, form, change):
        # 管理站点中点击保存，触发的自动执行的函数，钩子
        # request:本次客户端提交的请求对象
        # obj：本次操作的模型类实例对象
        # form:本次客户端提交的表单数据
        # change：值为True，表示更新数据，值为false：添加/新增数据
        # Add update
        obj.save()
        # 同步记录到redis中
        redis = get_redis_connection('coupon')
        if obj.use_status == 0 and obj.use_time == None:
            pipe = redis.pipeline()
            pipe.multi()
            # 首先存储数据结构 构建
            # 优惠券为一个对象 属性较多
            coupon_dict = {
                "coupon_id": obj.coupon.id,
                "name": obj.coupon.name,
                "discount": obj.coupon.discount,
                "get_discount_display": obj.coupon.get_discount_display(),
                "coupon_type": obj.coupon.coupon_type,
                "get_coupon_type_display": obj.coupon.get_coupon_type_display(),
                "start_time": obj.coupon.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": obj.coupon.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "get_type": obj.coupon.get_type,
                "get_get_type_display": obj.coupon.get_get_type_display(),
                "condition": obj.coupon.condition,
                "sale": obj.coupon.sale,
                "to_diretion": json.dumps(list(obj.coupon.to_diretion.values("diretion__id", "diretion__name"))),
                "to_category": json.dumps(list(obj.coupon.to_category.values("category__id", "category__name"))),
                "to_course": json.dumps(list(obj.coupon.to_course.values("course__id", "course__name"))),
            }
            # 专业、分类、课程
            print(f"添加的用户ID:{str(obj.user.id)}")
            pipe.hset(f"{obj.user.id}:{obj.id}", mapping = coupon_dict)
            print(f"打印redis存储的Key:{obj.user.id}:{obj.id}")
            
            # 过期时间
            # setex key 100 value
            from datetime import datetime
            # redis: 给任意类型的key设置过期时间
            # 设置当前用户优惠券有效期
            pipe.expire(f"{obj.user.id}:{obj.id}", int(obj.coupon.ent_time.timestamp()-datetime.now().timestamp()))
            pipe.execute()
        else:
            redis.delete(f"{obj.user.id}:{obj.id}")
    
    def delete_model(self, request, obj):
        """删除记录时候自动执行的钩子函数"""
        # 管理站点中删除当前优惠券，redis中也需要删除
        redis = get_redis_connection("coupon")
        redis.delete(f"{obj.user.id}:{obj.id}")
        obj.delete()
    
    # 数据导入，站点管理、获取优惠券、过滤有效优惠券
    def delete_queryset(self, request, queryset):
        # 列表页面中进行删除记录，选择可能是多条数据
        redis = get_redis_connection("coupon")
        # 遍历集合queryset
        for qs in queryset:
            redis.delete(f"{qs.user.id}:{qs.id}")
        queryset.delete()

admin.site.register(models.CouponLogModel, CouponLogModelsAdmin)

# 优惠券在数据库存储中，也可以在reids存储一份