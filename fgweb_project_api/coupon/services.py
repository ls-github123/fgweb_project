from django_redis import get_redis_connection
import json

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