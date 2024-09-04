from django.db import models
from fgweb_project_api.settings.utils.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from stdimage import StdImageField # 导入图片处理-缩略原图
from django.utils.safestring import mark_safe
# 方向列表\\\\专业列表

class CourseDirectionModel(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='方向名称')
    remark = RichTextUploadingField(default='', blank=True, null=True, verbose_name='方向描述信息')
    recomment_home_hot = models.BooleanField(default=False, verbose_name='是否推荐到首页最热栏目')
    recomment_home_top = models.BooleanField(default=False, verbose_name='是否推荐到首页必学栏目')
    
    class Meta():
        db_table = 'fg_course_direction'
        verbose_name_plural = '方向'
        
# 课程分类
class CourseCategoryModel(BaseModel):
    name = models.CharField(max_length=200, unique=True, verbose_name='分类名称')
    remark = RichTextUploadingField(default='', blank=True, null=True, verbose_name='分类描述信息')
    # 外键
    direction = models.ForeignKey(CourseDirectionModel, related_name='category_list', null=True, on_delete=models.DO_NOTHING, verbose_name='方向')
    
    class Meta():
        db_table= 'fg_course_category'
        verbose_name_plural = '课程分类'
    def __str__(self):
        return self.name
    
# 讲师模型类
class TeacherModel(BaseModel):
    ROLE_CHOICES = {
        (0,'讲师'),
        (1,'导师'),
        (2,'班主任')
    }
    role = models.SmallIntegerField(choices=ROLE_CHOICES, default=0, verbose_name='讲师身份')
    title = models.CharField(max_length=100, verbose_name='职位、职称')
    signature = models.CharField(max_length=255, blank=True, null=True, verbose_name='导师签名')
    # 改写
    # avatar = models.ImageField(upload_to='avatar/%Y/', null=True, verbose_name='讲师头像')
    avatar = StdImageField(upload_to='avatar/%Y/', null=True, verbose_name='讲师头像',
                           variations={ # 定义图片尺寸
                                    'thumb_800x800':{'width':800,'height':800}, # 'large': (600, 400)
                                    'thumb_400x400':{'width':400,'height':400},# 'thumbnail': (100, 100, True)
                                    'thumb_50x50':{'width':50,'height':50},# 'medium': (300, 200)
                           }, delete_orphans=True)
    brief = RichTextUploadingField(max_length=255, verbose_name='讲师描述')
    
    class Meta():
        db_table = "fg_teacher"
        verbose_name_plural = "讲师信息"
    def __str__(self):
        return self.name
    
    def avatar_small(self):
        # print('小图标配置....')
        # 管理站点不支持展示图片, return给管理站点提供image标签
        return mark_safe(f'<img style="border-radius:100%" alt=" " src="{ self.avatar.thumb_50x50.url }"></img>')
    # 图片描述
    avatar_small.short_description = '头像图片'
    # 图片显示控制
    avatar_small.allow_tags = True
    # 设置排序顺序
    avatar_small.admin_order_field = 'avatar'
    
    def avatar_large(self):
        # print('小图标配置.....')
        # 管理站点不支持展示图片, return给管理站点提供一个image标签
        return mark_safe(f'<img style="border-radius:100%" alt="头像" src="{ self.avatar.thumb_800x800.url }"></img>')
    # 图片描述
    avatar_large.short_description = '头像图片'
    # 图片显示控制
    avatar_large.allow_tags = True
    # 设置排序顺序
    avatar_large.admin_order_field = "avatar"
    

class CourseModel(BaseModel):
    COURSE_TYPE_CHOICES = {
        (0, '付费购买'),
        (1, '会员专享'),
        (2, '学位课程'),
    }
    LEVEL_CHOICES = {
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    }
    STATUS_CHOICES = {
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    }
    
    course_cover = models.ImageField(upload_to="course/cover/",blank=True,null=True,verbose_name="封面图片")
    course_video = models.FileField(upload_to="course/video/",blank=True,null=True,verbose_name="封面视频")
    course_type = models.SmallIntegerField(choices=COURSE_TYPE_CHOICES,default=0,verbose_name="付费课程")
    level = models.SmallIntegerField(choices=LEVEL_CHOICES,default=0,verbose_name="难度等级")
    description = RichTextUploadingField(null=True,blank=True,verbose_name="详情介绍")
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=0,verbose_name="课程状态")
    pub_date  =models.DateField(auto_now_add=True,verbose_name="发布日期")
    period = models.IntegerField(default=7,verbose_name="建议学习周期（天）")
    attachment_path = models.FileField(max_length=300,blank=True,null=True,verbose_name="课件路径") #课程路径
    attachment_link = models.CharField(max_length=300,blank=True,null=True,verbose_name="课件路径")# 可见连接
    students = models.IntegerField(default=0,verbose_name="学习人数")# 学习人数
    lessons = models.IntegerField(default=0,verbose_name="总课时数量")
    pub_lessons = models.IntegerField(default=0,verbose_name="已更新的课时数量")
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name="课程价格")
    credit = models.IntegerField(default=0,null=True,blank=True,verbose_name="积分兑换")
    recomment_home_hot = models.BooleanField(default=False,verbose_name="是否推荐到首页最热栏目")

    recomment_home_top = models.BooleanField(default=False,verbose_name="是否推荐到首页必须栏目")
    # 是否推荐到首页必学、首页最热
    # 外键
    direction = models.ForeignKey(CourseDirectionModel,related_name="course_list",on_delete=models.DO_NOTHING,null=True,blank=True,db_constraint=False,verbose_name="方向")
    category = models.ForeignKey(CourseCategoryModel,related_name='course_list',null=True,blank=True,on_delete=models.DO_NOTHING,db_constraint=False,verbose_name="分类")
    teacher = models.ForeignKey(TeacherModel,related_name="course_list",on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="讲师")
    class Meta():
        db_table = "fg_course_info"
        verbose_name_plural = "课程信息"
    def __str__(self):
        return self.name
    
    @property
    def discount(self):
        # 返回折扣信息
        return {
            "type":"0", # 满减\折扣 免费
            "expire":"1000", # 过期时间
            "price":"188" # 优惠价格
        }