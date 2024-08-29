from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users import models
import re

# 自定义序列化器，实现自定义载荷信息的添加
class CoustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # 根据用户，获取token
        token = super().get_token(user)

        token['username'] = user.username
        token['avatar'] = str(user.avatar)
        token['money'] = str(user.money)
        token['credit'] = str(user.credit)

        return token
    
# 自定义用户账户注册序列化器及校验规则
class RegisterSerializer(serializers.ModelSerializer):
    # re_password(密码确认)、sms_code(验证码)仅在反序列化过程中使用
    re_password = serializers.CharField(required=True, write_only=True, min_length=6, max_length=16)
    sms_code = serializers.CharField(required=True, write_only=True)
    
    # 令牌token和refresh仅在序列化时使用
    # 用户注册成功后返回登录令牌
    token = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    
    class Meta():
        model = models.UsersModel
        fields = ['mobile', 'password', 're_password', 'sms_code', 'token', 'refresh']
        
        # 为模型类属性添加额外约束条件
        extra_kwargs = {
            "mobile":{
                "required":True,
                "write_only":True
            },
            
            "password":{
                "required":True,
                "write_only":True,
                "min_length":6,
                "max_length":16
            }
        }
        
    def validate(self, attrs):
        # 自定义校验规则
        # 校验传递数据，是否满足业务需求
        mobile = attrs.get('mobile', None)
        # 判断手机号是否满足规则
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            raise serializers.ValidationError(detail="手机号格式错误", code="mobile")
        print('-----手机号校验通过-----')
        
        password = attrs.get('password')
        re_password = attrs.get('re_password')
        
        if password != re_password:
            raise serializers.ValidationError(detail="两次密码输入不一致,请重新输入", code="password")
        print('------密码校验通过------')
        
        # 验证码获取/校验模块
        # 开发中
        # ------------------
        
        try:
            # 用户已存在，抛出异常
            models.UsersModel.objects.get(mobile__exact=mobile)
            raise serializers.ValidationError(detail="用户已存在！", code="mobile")
        except models.UsersModel.DoesNotExist:
            print('-----数据库中未找到用户信息,执行注册通过-----')
        
        # 执行数据库操作
        attrs.pop('re_password')
        attrs.pop('sms_code')
        return attrs
    
    def create(self, validated_data):
        mobile = validated_data.get('mobile')
        password = validated_data.get('password')
        
        # 注册新用户, 初始化用户信息
        user = models.UsersModel.objects.create_user(
            mobile = mobile,
            password = password,
            # 生成默认用户名
            # 引入随机模块或直接以手机号代替
            username = mobile,
            money = 0,
            credit = 0,
            # 用户头像模块
            avatar = "avatar/2024/default.jpg",
        )
        
        # 返回token、refresh
        # 手动签发token
        refresh = CoustomTokenObtainPairSerializer.get_token(user)
        user.refresh = str(refresh)
        user.token = str(refresh.access_token)
        return user