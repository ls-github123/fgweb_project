from django.db import models
from fgweb_project_api.settings.utils.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from stdimage import StdImageField # 导入图片处理-缩略原图
from django.utils.safestring import mark_safe
import datetime
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
        # 查询有效活动
        now_time = datetime.datetime.now()
        last_activate = self.price_list.filter(activate__start_time__lt = now_time, activate__end_time__gt = now_time).order_by('-id').first()
        type_text = "优惠类型"
        expire = -1
        price = 0 # 优惠后的价格
        if last_activate:
            # 有优惠活动 -- 获取当前课程对应所有优惠信息
            print(last_activate.activate.name)
            print(last_activate.activate.end_time)
            print(last_activate.discount.discount_type.name)
            # 获取优惠信息
            type_text = last_activate.discount.discount_type.name
            # 过期时间
            expire = last_activate.activate.end_time.timestamp() - now_time.timestamp()
            
            # 计算价格
            course_price = float(self.price) # 当前课程价格
            # 有限考虑 条件:门槛
            condition_price = float(last_activate.discount.condition)
            # 判断当前课程价格 是否大于优惠门槛
            if course_price >= condition_price:
                # 计算当前课程参与得优惠，以及优惠后得价格
                sale = last_activate.discount.sale

                if sale == "0":
                    # 免费
                    price = 0
                elif sale[0] == "*":
                    # 折扣
                    price = course_price * float(sale[1:])

                    # *0.2
                    # -100
                elif sale[0] == "-":
                    price = course_price - float(sale[1:])

                price = float(f"{price:.2f}")
            # else:
            #     price = course_price
        else:
            print('当前课程没有参与优惠活动.....')
            price = self.price
        return {
            "type":type_text,  #  满减、折扣   免费
            "expire":expire,  # 过期时间
            "price":price   #  优惠价格
        }
        
# 优惠活动表
class ActivateModel(BaseModel):
    start_time = models.DateTimeField('开始时间', default=datetime.datetime.now())
    end_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='结束时间')
    description = RichTextUploadingField(blank=True,null=True,verbose_name='活动介绍')
    remark = models.CharField(max_length=300,blank=True,null=True,verbose_name="备注信息")
    class Meta():
        db_table = 'fg_activate'
        verbose_name_plural = '优惠活动'
# 优惠类型
# 满减、折扣
class DiscountTypeModel(BaseModel):
    remark = models.CharField(max_length=300,blank=True,null=True,verbose_name="备注信息")
    class Meta():
        db_table = 'fg_discount_type'
        verbose_name_plural = '优惠类型'

# 折扣表
class DiscountModel(BaseModel):
    discount_type = models.ForeignKey(DiscountTypeModel,on_delete=models.CASCADE,db_constraint=False,verbose_name="优惠类型")

    # 优惠限制条件
    #不填写，表示优惠没有门槛
    condition = models.IntegerField(blank=True,default=0,verbose_name='优惠条件')

    # 定义折扣
    # 人为定义一个折扣
    sale = models.CharField(max_length=50,verbose_name="优惠公式")
    # 0表示免费
    # * 表示折扣    *0.8  表示打8折
    # -表示满减   -100   满足条件，减100
    def __str__(self):
        return "优惠：%s - 条件 %s 优惠方式：%s" % (self.discount_type.name,self.condition,self.sale)
    class Meta():
        db_table = "fg_discount"
        verbose_name_plural = "折扣表"

class CourseActivateModel(BaseModel):
    activate = models.ForeignKey(ActivateModel,on_delete=models.CASCADE,related_name='price_list',db_constraint=False,verbose_name="活动")
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE,related_name="price_list",db_constraint=False,verbose_name='课程')
    discount = models.ForeignKey(DiscountModel,on_delete=models.CASCADE,related_name="price_list",db_constraint=False,verbose_name='折扣')
    class Meta:
        db_table = "fg_course_activate_price"
        # 课程活动价格表
        verbose_name_plural= "课程活动"
    def __str__(self):
        return "课程: %s -活动: %s - 折扣：%s" % (self.course.name,self.activate.name,self.discount.sale)
    
    
# 课程章节
# 章节
class CourseChapterModel(BaseModel):
    orders = models.SmallIntegerField(default=1, verbose_name='第几章')
    summary = RichTextUploadingField(blank=True, null=True, verbose_name='章节描述')
    pub_date = models.DateField(auto_now_add=True, verbose_name='章节发布时间')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, db_constraint=False, verbose_name='课程')
    class Meta():
        db_table = 'fg_course_chapter'
    
    def __str__(self):
        return "第 %d 章 - %s" % (self.orders, self.name)

# json：
    # [{"":""},{"":"",},]
    # ["age":18,"height":19,"birthday":2093,{"":""},{}]
    
    def get_lesson_list(self):
        lesson_list = self.lesson_list.filter(is_deleted=False, is_show=True).order_by('orders')
        result_list = []
        for ls in lesson_list:
            # 将拼好得字典格式得数据，转换成json格式
            # Response()
            # JsonResponse()
            result_list.append({
                "id":ls.id,
                "name":ls.name,
                "orders":ls.orders,
                "duration":ls.duration,
                "pub_date":ls.pub_date,
                "lesson_link":ls.lesson_link,
                "free_trail":ls.free_trail,
            })
        return result_list
    

class CourseLessonsModel(BaseModel):
    # 课时小节
    # 类型
    LESSON_TYPE_CHOICES = {
        (0,'文档'),
        (1,'练习'),
        (2,'视频'),
    }
    # 时长
    orders = models.SmallIntegerField(default=1, verbose_name='第几节')
    lesson_type = models.SmallIntegerField(choices=LESSON_TYPE_CHOICES, default=2, verbose_name='文档类型')
    duration = models.CharField(max_length=100, blank=True, null=True, verbose_name='课时时长')
    lesson_link = models.CharField(max_length=255, verbose_name='课时连接')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='课时发布时间')
    # 是否可以观看 -- 免费观看
    free_trail = models.BooleanField(default=False, verbose_name='是否可以免费试看')
    chapter = models.ForeignKey(CourseChapterModel, related_name='lesson_list', db_constraint=False, on_delete=models.CASCADE, verbose_name='章节')
    course = models.ForeignKey(CourseModel, related_name='lesson_list', db_constraint=False, on_delete=models.CASCADE, verbose_name='课程')
    
    class Meta():
        db_table = 'fg_course_lesson'
        verbose_name_plural = '课时'
    def __str__(self):
        return "第 %s 章 - 第 %s 课时 - %s" % (self.chapter.orders, self.orders, self.name)     