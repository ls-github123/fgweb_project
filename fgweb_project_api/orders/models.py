from django.db import models
from users.models import UsersModel
from course.models import CourseModel
from fgweb_project_api.settings.utils.models import BaseModel

# 数据库表
class OrdersModel(BaseModel):
    STATUS_CHOICES = [
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '已超时'),
    ]
    PAY_CHOICES = [
        (0, '支付宝'),
        (1, '微信'),
        (2, '余额'),
    ]
    # 订单总价(没有优惠)
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='订单总价')
    real_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='实付金额')
    order_number = models.CharField(max_length=64, verbose_name='订单号')
    # 订单状态
    order_status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0, verbose_name='订单状态')
    pay_type = models.SmallIntegerField(choices=PAY_CHOICES, default=0, verbose_name='支付方式')
    order_desc = models.TextField(null=True, blank=True, max_length=300, verbose_name='订单描述')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    credit = models.IntegerField(default=0, null=True, blank=True, verbose_name='积分')
    user = models.ForeignKey(UsersModel, related_name='user_orders', on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='用户')
    
    class Meta():
        db_table = 'fg_order'
        verbose_name_plural = '订单记录表'
    
    def __str__(self):
        return "%s 总价: %s, 实付金额: %s" % (self.name, self.total_price, self.real_price)
    
# 订单详情
class OrderDetaileModel(BaseModel):
    order = models.ForeignKey(OrdersModel, related_name='order_courses', on_delete=models.CASCADE, db_constraint=False, verbose_name='订单')
    course = models.ForeignKey(CourseModel, related_name='course_orders', on_delete=models.CASCADE, db_constraint=False, verbose_name='课程')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课程原价")
    real_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="优惠价格")
    discount_name = models.CharField(max_length=100, default="", verbose_name="优惠类型")
    
    class Meta:
        db_table = 'fg_order_course'
        verbose_name_plural = '订单详情'
        
    def __str__(self):
        return self.course.name