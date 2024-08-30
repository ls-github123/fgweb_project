# 阿里云短信验证码 API配置
from alibabacloud_tea_openapi import models as open_api_models # 初始化配置对象
from django.conf import settings
from alibabacloud_dysmsapi20170525.client import Client as DysmsapiClient
from alibabacloud_dysmsapi20170525 import models as sms_models
from Tea.exceptions import UnretryableException, TeaException
import json

# import random

# re_code = random.randint(10000,99999)
# print(re_code)
# template_param = {"code":re_code}

# 初始化配置对象
aliyun_server = settings.ALIYUNSMS_SERVER # 从dev设置中获取设置参数
def init_client():
    config_obj = open_api_models.Config(
        # access_key_id = aliyun_server.get('access_key_id'),
        access_key_id = aliyun_server.get('access_key_id'),
        # access_key_secret = aliyun_server.get('access_key_secret')
        access_key_secret = aliyun_server.get('access_key_secret')
    )
    # 指向阿里云域名
    config_obj.endpoint = 'dysmsapi.aliyuncs.com'
    return DysmsapiClient(config_obj)

# 短信发送接口
def send_sms(phone_number, template_param):
    client = init_client()
    request = sms_models.SendSmsRequest()
    
    # 设置请求参数
    request.phone_numbers = phone_number # 接收短信手机号
    request.sign_name = aliyun_server.get('sign_name') # 短信签名名称
    request.template_code = aliyun_server.get('template_code') # 短信模板代码
    request.template_param = json.dumps(template_param) # 模板变量对应值 转换为json字符串
    
    try:
        # 发送短信
        response = client.send_sms(request)
        print(response)
        # 阿里云返回的消息体
        response_body = response.body
        print(response_body)
        
        # 打印成功或失败状态
        if response_body.code == 'OK':
            print("验证短信发送成功")
            print("RequestID:", response_body.request_id)
            print("BizId:", response_body.biz_id)
        else:
            print("验证短信发送失败!")
            print("错误代码:", response_body.code)
            print("错误信息:", response_body.message)
        return response_body.code
    
    except UnretryableException as e:
        print(f"网络异常:{e}")
    except TeaException as e:
        print(f"业务异常:{e}")
    except Exception as e:
        print(f"其他异常:{e}")
        return None