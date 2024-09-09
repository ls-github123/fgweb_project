from django.contrib import admin
from coupon.models import CouponModels,CouponCourseDirectionModel,CouponCourseCategoryModel,CouponCourseModel,CouponLogModel
from django_redis import get_redis_connection
import json
# Register your models here.


# 方向
# 外键关联显示
class CouponDirectionInline(admin.TabularInline):
    model = CouponCourseDirectionModel
    fields = ['id','direction']


class CouponCategoryInline(admin.TabularInline):
    model = CouponCourseCategoryModel
    fields = ['id','category']

class CouponCourseInline(admin.TabularInline):
    model = CouponCourseModel
    fields = ['id','course']


# 优惠券自定义类
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','start_time','end_time'
                    ,'total','has_total','coupon_type','get_type']
    # 实现外键关联的
    inlines = [CouponDirectionInline,CouponCategoryInline,CouponCourseInline]
admin.site.register(CouponModels,CouponModelAdmin)

# admin.site.register(CouponCourseDirectionModel)
# admin.site.register(CouponCourseCategoryModel)
# admin.site.register(CouponCourseModel)


class CouponLogModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','coupon','use_time','use_status']
    def save_model(self, request, obj, form, change):
        # 管理站点点击保存，自动触发的函数，钩子函数
        # request: 本次客户端提交的请求对象
        # obj : 本次操作的模型类实例对象
        # form:提交的表单数据
        # change: true 表示更新数据，  false 添加新增数据
        obj.save()
        redis = get_redis_connection('coupon')
        if obj.use_status == 0 and obj.use_time == None:
            pipe = redis.pipeline()
            pipe.multi()
            # 往reids中，存数据，
            # 构建数据存储类型，属性全部放如reids中
            coupon_dict = {
                "coupon_id":obj.coupon.id,
                "name":obj.coupon.name,
                "discount":obj.coupon.discount,
                "get_discount_display":obj.coupon.get_discount_display(),
                "coupon_type":obj.coupon.coupon_type,
                "get_coupon_type_display":obj.coupon.get_coupon_type_display(),
                "get_type":obj.coupon.get_type,
                "get_get_type_display":obj.coupon.get_get_type_display(),
                "start_time":obj.coupon.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time":obj.coupon.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "condition":obj.coupon.condition,
                "sale":obj.coupon.sale,
                "to_direction":json.dumps(list(obj.coupon.to_direction.values('direction__id','direction__name'))),
                "to_category":json.dumps(list(obj.coupon.to_category.values('category__id','category__name'))),
                "to_course":json.dumps(list(obj.coupon.to_course.values('course__id','course__name'))),
                # json     list
            }
            # 用户id
            # obj.user.id
            print('用户id:',obj.user.id)

            # pipe.hset(f"{obj.user.id}:{obj.id}","coupon_id",obj.coupon.id)
            # pipe.hset(f"{obj.user.id}:{obj.id}","name",obj.coupon.name)

            pipe.hset(f"{obj.user.id}:{obj.id}",mapping=coupon_dict)
            print("打印存入redis中的key")
            print(f"{obj.user.id}:{obj.id}")

            # 设置过期时间
            from datetime import datetime
            # 数据类型，都可以过期时间，，根据key设置
            pipe.expire(f"{obj.user.id}:{obj.id}",int(obj.coupon.end_time.timestamp()-datetime.now().timestamp()))
            pipe.execute()
        else:
            redis.delete(f"{obj.user.id}:{obj.id}")

    def delete_model(self, request, obj):
        redis = get_redis_connection('coupon')
        redis.delete(f"{obj.user.id}:{obj.id}")
        obj.delete()

    def delete_queryset(self, request, queryset):
        redis = get_redis_connection("coupon")
        for qs in queryset:
            redis.delete(f"{qs.user.id}:{qs.id}")
        queryset.delete()


admin.site.register(CouponLogModel,CouponLogModelAdmin)