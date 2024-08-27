from django.db import models

# 定义公共抽象模型
class BaseModel(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True, blank=None, verbose_name='名称')
    orders = models.IntegerField(default=0, verbose_name='序号')
    is_show = models.BooleanField(default=True, verbose_name='是否展示')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        # 设置当前抽象类，非真实数据模型
        abstract = True
        
    def __str__(self):
        return self.name