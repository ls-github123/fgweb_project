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
        
# 轮播图模型类
class BannerModel(BaseModel):
    image = models.ImageField(upload_to="banner/%Y")
    link = models.CharField(max_length=300, verbose_name="是否为外部链接")
    note = models.CharField(max_length=100, verbose_name="备注信息")
    is_http = models.BooleanField(default=False, verbose_name="是否为外部链接", help_text="站点外部连接：http://www.baidu.com <br>站点内的连接：/home/detail/")
    
    class Meta:
        db_table = 'fg_banner'
        managed = True
        verbose_name = '轮播广告'
        verbose_name_plural = '轮播广告'