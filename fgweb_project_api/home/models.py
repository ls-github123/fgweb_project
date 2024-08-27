from django.db import models
from fgweb_project_api.settings.utils.models import BaseModel

class NavModel(BaseModel):
    POSITION_CHOICES = {
        (0, "顶部导航"),
        (1, "底部导航")
    }

    link = models.CharField('导航连接', max_length=100)
    is_http = models.BooleanField('是否为外部连接', default=False)
    # 判定头部和底部导航
    postion = models.ImageField('导航位置区分', choices=POSITION_CHOICES, default=0)
    
    class Meta:
        db_table = 'fg_nav'
        managed = True
        verbose_name = '导航菜单'
        verbose_name_plural = '导航菜单'