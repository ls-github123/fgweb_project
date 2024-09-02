import random # 随机数模组
from rest_framework.views import APIView
from rest_framework.response import Response
# from fgweb_project_api.settings.utils.aliyun_sms_server import send_sms
from django.conf import settings
from rest_framework import status
from django_redis import get_redis_connection
# 导入celery异步任务
from celery_module.sms.tasks import send_message

class SMSApiViews(APIView):
    def get(self, request, mobile):
        # 获取redis连接
        redis = get_redis_connection('sms_code')
        
        # 默认进入发送短信验证码操作,需要验证是否过期
        # 有限获取当前发送验证码，是否在间隔期
        res_interval = redis.ttl(f"interval_{mobile}")
        if res_interval != -2:
            return Response({"message":"上一验证码仍在有效期内,请勿频繁发送!"}, status=status.HTTP_400_BAD_REQUEST)
        
        aliyunsms = settings.ALIYUNSMS_SERVER
        sms_interval = aliyunsms.get('sms_interval') # 间隔时间, 以秒计算
        sms_expire = aliyunsms.get('sms_expire') # 有效时间, 以秒计算
        
        phone_number = mobile # 获取用户输入的手机号参数
        
        # 生成6位随机验证码
        re_code = f"{random.randint(100000, 999999):06d}"
        print(f"生成随机验证码:{re_code}")
        
        # 验证码有效时间 秒/60 转换为分 
        # 阿里云接口为分钟显示${time}, 有效期X分钟
        code_expire = int(sms_expire/60)
        
        # 短信模板变量对应值参数 ${code} ${time}
        template_param = {
            "code":re_code, # 生成的随机验证码
            "time":str(code_expire) # 验证码有效时间
        }
        
        # celery 执行异步任务
        send_message.delay(phone_number, template_param)
        # redis操作
        # 往redis中保存手机号与验证码
        # 使用redis提供的管道对象：pipeline 优化redis写入操作
        pipe = redis.pipeline()
        pipe.multi() #开始事务  保证命令一并发送到服务端，
        redis.setex(f"sms_{mobile}",sms_expire, re_code)
        redis.setex(f"interval_{mobile}",sms_interval,'-')
        # 提交事务，同时把暂存在pipeline对象中的多条命令，一次性提交给reids
        pipe.execute()
        
        return Response({"message": "短信发送成功"}, status=status.HTTP_200_OK)