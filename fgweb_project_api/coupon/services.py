from django_redis import get_redis_connection
import json
from course.models import CourseModel

# 获取当前用户所有优惠券
# 有效/无效
def get_user_coupon_list(user_id):
    # f"userid:coupon_id"
    redis = get_redis_connection('coupon')
    # 匹配获取当前redis中以user_id 开头的所有key
    coupon_list = redis.keys(f"{user_id}:*")
    coupon_id_list = [item for item in coupon_list]
    
    # 构建空列表 用于存储循环后的优惠券数据
    coupon_data = []
    for coupon_key in coupon_id_list:
        # 获取优惠券ID 默认生成字段
        coupon_item = {"user_coupon_id":int(coupon_key.split(":")[-1])}
        # 根据key 获取对应所有属性
        coupon_hash = redis.hgetall(coupon_key)
        for key, value in coupon_hash.items():
            key = key.decode()
            value = value.decode()
            # 如果key为外键，外键存放json格式数据
            # 需要将字符串转换python中的字典格式数据类型
            if key in ['to_direction', 'to_category', 'to_course']:
                # json.loads()方法 
                # 用于将符合JSON标准的字符串转换为Python数据结构
                #（常见的是转换为字典或列表）
                value = json.loads(value)
            coupon_item[key] = value
        coupon_data.append(coupon_item)
    return coupon_data
# [{"coupon_id":1,"name":'7天学费...'}，{"coupon_id":1,"name":'7天学费...'}]


def get_user_enable_coupon_list(user_id):
    # 获取指定用户当次下单的优惠券列表
    # 1.首先获取购物车中选中的商品
    redis = get_redis_connection('cart')
    # 获取购物车中所有选中的商品数据
    cart_hash = redis.hgetall(f"cart_{user_id}")
    
    # cart_1 1 0/1
    # 获取选中
    course_id_list = {int(key.decode()) for key, value in cart_hash.items() if value ==b'1'}
    # 根据课程id列表 获取对应课程
    course_list = CourseModel.objects.filter(id__in = course_id_list, is_deleted = False, is_show = True)
    
    # 通过课程列表 获取分类 id列表 方向id列表
    direction_id_list = set()
    category_id_list = set()
    
    for course in course_list:
        direction_id_list.add(int(course.direction.id))
        category_id_list.add(int(course.category.id))
        
    # 获取优惠券列表
    coupon_data = get_user_coupon_list(user_id)
    # 构建一个可用的优惠列表对象
    enable_coupon_list = []
    # 遍历优惠券数据
    for item in coupon_data:
        coupon_type = int(item.get('coupon_type'))
        if coupon_type == 0:
            item['enable_course'] = "__all__"
            enable_coupon_list.append(item)
        elif coupon_type == 1:
            # 方向优惠券
            coupon_direction = {direction_item['direction__id'] for direction_item in item.get("to_direction")}
            # 交集
            ret = coupon_direction & direction_id_list
            item['enable_course'] = { int(course.id) for course in course_list if course.direction.id in ret }
            enable_coupon_list.append(item)
        elif coupon_type == 2:
            # 分类
            coupon_category = {category_item['category__id'] for category_item in item.get("to_category")}
            print('打印优惠券对应的分类id列表')
            print(coupon_category)
            
            ret = coupon_category & category_id_list
            if len(ret) > 0:
                item['enable_course'] = {int(course.id) for course in course_list if course.category.id in ret}
                enable_coupon_list.append(item)
        elif coupon_type == 3:
            coupon_course = {course_item['coures_id'] for course_item in item.get("to_course")}
            ret = coupon_course & course_id_list
            if len(ret) > 0:
                # 遍历所有课程列表
                item['enable_course'] = {int(course.id) for course in course_list if course.id in ret}
                enable_coupon_list.append(item)
    return enable_coupon_list