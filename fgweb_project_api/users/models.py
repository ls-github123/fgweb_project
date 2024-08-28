from django.db import models
from django.contrib.auth.models import User, AbstractUser

class UsersModel(AbstractUser):
    # 新增用户自定义字段
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    avatar = models.ImageField(upload_to="avatar/%Y/", null=True, blank=True, verbose_name='用户头像')
    nickname = models.CharField(max_length=50, default="", null=True, verbose_name='用户昵称')
    money = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name='钱包余额')
    credit = models.IntegerField(default=0, verbose_name='用户积分')
    
    class Meta:
        db_table = 'fg_users'
        managed = True
        verbose_name = '用户表'
        verbose_name_plural = '用户表'