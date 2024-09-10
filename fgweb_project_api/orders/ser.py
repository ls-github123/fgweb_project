 
from rest_framework import serializers
from orders.models import OrdersModel
from django_redis import get_redis_connection
from django.db import transaction

class OrderModelSerializer(serializers.ModelSerializer):
    user_coupon_id = serializers.IntegerField(write_only=True, default=None)
    class Meta():
        # 订单超时
        fields = ['pay_type', 'id', 'user_coupon_id', 'credit']
        extra_kwargs = {
            "pay_type":{"write_only":True},
            "credit":{"write_only":True},
        }
    def create(self, validated_data):
        # 积分获取和判断
        # 优惠券获取和判断
        user = self.context['request'].user
        user_id = user.id
        
        # 购买课程 -- 获取购物车中课程
        redis = get_redis_connection('cart')
        # 获取当前用户课程列表
        cart_hash = redis.hgetall(f"cart_{user_id}")
        
        if len(cart_hash) < 1:
            raise serializers.ValidationError(detail="购物车没有数据", code="cart_enpty")
        
        # 获取前端传递的使用积分
        use_credit = validated_data.get('credit', 0)
        # 判断当前用户是否选择积分, 且积分是否足够划扣
        if use_credit > 0 and use_credit > user.credit:
            raise serializers.ValidationError(detail='您的积分不足,请重新选择', code='credir_error')
        
        # 开启数据库事务操作
        # 原子性 隔离性 一致性 持久性
        with transaction.atomic():
            # 创建一个还原点
            t1 = transaction.savepoint()
            try:
                pass
            except Exception as es:
                print('订单创建失败...')
                print(es)
                transaction.savepoint_rollback(t1)
                raise serializers.ValidationError(detail='订单生成失败', code='order_error')