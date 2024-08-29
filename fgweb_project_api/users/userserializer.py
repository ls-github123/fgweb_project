from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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