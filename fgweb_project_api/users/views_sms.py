import random # 随机数模组
from rest_framework.views import APIView
from rest_framework.response import Response
from fgweb_project_api.settings.utils.aliyun_sms_server import send_sms
from django.conf import settings
from rest_framework import status
from django_redis import get_redis_connection
# 导入celery异步任务
from celery_module.sms.tasks import send_message
from celery.result import AsyncResult


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
        
        # 调用接口 尝试发送验证码
        # res = send_sms(phone_number, template_param)
        
        # 向redis数据库中保存手机号与验证码
        # redis.setex(name, time, value)
        # name-要设置的键  time-该键过期时间(秒为单位) value-写入的内容(随机生成的验证码)
        
        # if res == "OK":
        #     # 短信发送成功，保存验证码到 Redis
        #     # sms_{mobile}键 通过手机号来查找对应的验证码
        #     redis.setex(f'sms_{mobile}', sms_expire, re_code)
        #     # interval_{mobile}键 记录发送验证码的时间间隔
        #     redis.setex(f'interval_{mobile}', sms_interval, '-')
        #     return Response({"message": "短信验证码发送成功"}, status=status.HTTP_200_OK)
        # else:
        #     # 短信发送失败，返回错误信息
        #     return Response({"message": f"短信验证码发送失败! 错误代码: {res}"}, status=status.HTTP_400_BAD_REQUEST)
        
        # 调用celery异步任务
        task = send_message.delay(phone_number, template_param)
        
        # 检查任务执行状态
        result = AsyncResult(task.id)
        try:
            task_result = result.get(timeout=10)  # 等待任务结果

            # 检查 task_result 的类型
            if isinstance(task_result, dict):
                # 如果 task_result 是字典
                if task_result.get('Code') == 'OK':
                    # 向 redis 数据库中保存手机号与验证码
                    pipe = redis.pipeline()
                    pipe.multi()  # 开始事务
                    redis.setex(f"sms_{mobile}", sms_expire, re_code)
                    redis.setex(f"interval_{mobile}", sms_interval, '-')
                    pipe.execute()  # 提交事务
                    return Response({"message": "验证码发送成功"}, status=status.HTTP_200_OK)
                else:
                    # 如果 Code 不是 'OK'
                    return Response({"message": task_result.get('Message', '未知错误')}, status=status.HTTP_400_BAD_REQUEST)
            elif isinstance(task_result, str):
                # 如果 task_result 是字符串
                return Response({"message": task_result}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # 如果 task_result 既不是字典也不是字符串
                return Response({"message": "未知错误"}, status=status.HTTP_400_BAD_REQUEST)
        except TimeoutError:
            return Response({"message": "任务执行超时"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)