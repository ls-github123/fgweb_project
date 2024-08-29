# 手动签发token jwt生成

# 导入Django运行环境
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fgweb_project_api.settings.dev')
django.setup()

from users.models import UsersModel
from rest_framework_simplejwt.tokens import RefreshToken

try:
    # 授权获取登录用户
    user = UsersModel.objects.get(id=1)
    # 根据用户，获取刷新token实例
    refresh = RefreshToken.for_user(user)
    print(refresh)
    refresh_token = str(refresh)
    
    access_token = refresh.access_token
    print('-------------')
    print(access_token)
except UsersModel.DoesNotExist:
    print('用户不存在,签发失败!')