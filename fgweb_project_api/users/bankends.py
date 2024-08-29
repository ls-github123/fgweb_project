from django.contrib.auth.backends import ModelBackend
from users.models import UsersModel
from django.db.models import Q

def get_user_by_accout(accout):
    user = UsersModel.objects.filter(Q(username=accout) | Q(mobile=accout) | Q(email=accout)).first()
    return user

class CoustomModelBancked(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 用户名，查询用户。判断密码是否正确
        if username is None:
            username = kwargs.get(UsersModel.USERNAME_FIELD)
        if username is None and password is None:
            return
        # 手机号，邮箱 用户名
        user = get_user_by_accout(username)
        # 条件查询出用户，  根据用户判断密码是否正确，      根据用户模型，查看是否是活跃用户
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user