from django.db import models
from fgweb_project_api.settings.utils.models import BaseModel
from course.models import CourseDirectionModel,CourseCategoryModel,CourseModel
from users.models import UsersModel
# Create your models here.

# 优惠券模型类
    # 优惠类型
    # 获取方式 ： 系统赠送，用户领取
    # 总数量
    # 剩余数量
    # 使用时间
    # 过期时间
    # 使用优惠券的价格限制
    # 限制领取数量
    # 折扣：具体优惠  sale

class CouponModels(BaseModel):
    DISCOUNT_CHOICES = {
        (0,'减免'),
        (1,'折扣')
    }
    TYPE_CHOICES = {
        (0,'通用类型'),
        (1,'指定方向专业'),
        (2,'指定课程分类'),
        (3,'指定课程'),
    }
    GET_CHOICES = {
        (0,'系统赠送'),
        (1,'用户领取'),
    }
    discount = models.SmallIntegerField(choices=DISCOUNT_CHOICES,default=1, verbose_name="优惠方式")
    coupon_type =models.SmallIntegerField(choices=TYPE_CHOICES,default=0,verbose_name="优惠券类型")
    get_type =models.SmallIntegerField(choices=GET_CHOICES,default=0,verbose_name="优惠券领取方式")
    total = models.IntegerField(blank=True,null=True,default=100,verbose_name="发放数量")
    has_total = models.IntegerField(blank=True,null=True,default=100,verbose_name="剩余数量")
    start_time = models.DateTimeField(verbose_name="使用时间")
    end_time = models.DateTimeField(verbose_name="过期时间")
    condition = models.IntegerField(blank=True,default=0,verbose_name="满足优惠券使用的价格条件")
    per_limit = models.SmallIntegerField(default=1,verbose_name="每人限制领取的数量")
    sale = models.TextField(verbose_name="优惠公式",help_text="*表示折扣，例如：*0.8表示打8折"
                                                              "-表示满减，-100表示总价基础上减少100块人民币")
    class Meta:
        db_table = 'fg_coupon'
        verbose_name_plural = "优惠券"

# 优惠券与方向
class CouponCourseDirectionModel(models.Model):
    # 优惠券
    coupon = models.ForeignKey(CouponModels,on_delete=models.CASCADE,related_name='to_direction',db_constraint=False,verbose_name="优惠券")
    # 专业  方向
    direction = models.ForeignKey(CourseDirectionModel,on_delete=models.CASCADE,related_name="to_coupon",db_constraint=False,verbose_name="专业方向")
    # 创建，添加时间
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    class Meta():
        db_table = "fg_coupon_course_direction"
        verbose_name_plural = "优惠券与专业方向"


# 优惠券与分类
class CouponCourseCategoryModel(models.Model):

    category = models.ForeignKey(CourseCategoryModel,on_delete=models.CASCADE,related_name='to_coupon',db_constraint=False,verbose_name='课程分类')
    # 优惠券
    coupon = models.ForeignKey(CouponModels,on_delete=models.CASCADE,related_name="to_category",db_constraint=False,verbose_name="优惠券")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    class Meta():
        db_table = "fg_coupon_course_category"
        verbose_name_plural = '优惠券与课程分类'


# 优惠券与课程
class CouponCourseModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='to_coupon',
                                 db_constraint=False, verbose_name='课程')
    # 优惠券
    coupon = models.ForeignKey(CouponModels, on_delete=models.CASCADE, related_name="to_course", db_constraint=False,
                               verbose_name="优惠券")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    class Meta():
        db_table = "fg_coupon_course"
        verbose_name_plural = "优惠券与课程信息"



# 优惠券日志管理
class CouponLogModel(BaseModel):
    USE_CHOICES = {
        (0,'未使用'),
        (1,'已使用'),
        (2,'已过期'),
    }
    user = models.ForeignKey(UsersModel,on_delete=models.CASCADE,related_name="to_conpon",db_constraint=False,verbose_name="用户")
    coupon = models.ForeignKey(CouponModels,on_delete=models.CASCADE,related_name="to_user",db_constraint=False,verbose_name="优惠券")
    # 订单中使用优惠券  ----   等待开发
    # orders =
    use_time = models.DateTimeField(null=True,blank=True,verbose_name="使用时间")
    use_status = models.SmallIntegerField(choices=USE_CHOICES,null=True,blank=True,default=0,verbose_name="使用状态")
    class Meta():
        db_table = "fg_coupon_log"
        verbose_name_plural = "优惠发放与日志类"
    def __str__(self):
        return f"{self.coupon.name}发放和使用日志"
