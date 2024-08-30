from alibabacloud_tea_openapi import models as open_api_models
import random

# python-decouple包, 导入本地.env配置信息(mysql数据库地址、密码、端口等),该信息不会被git同步
from decouple import config
# 初始化阿里云短信平台配置对象
config_obj = open_api_models.Config(
    # 您的AccessKey ID,
    access_key_id = config('ACCESS_KEY_ID'),
    # 您的AccessKey Secret,
    access_key_secret = config('ACCESS_KEY_SECRET')
)
# 访问的域名
config_obj.endpoint = 'dysmsapi.aliyuncs.com'

# 实例化客户端
from alibabacloud_dysmsapi20170525.client import Client as Client
from alibabacloud_dysmsapi20170525 import models as models

client = Client(config_obj)

# 创建对应API request
request = models.SendSmsRequest()
request.phone_numbers = "18795190581"
request.sign_name = "浮光web"
request.template_code = "SMS_472420165"

# 使用 json.dumps 转换为 JSON 字符串
re_code = f'{random.randint(1000,9999)}'
print(re_code)
import json
template_param = {
    "code":re_code
}
request.template_param = json.dumps(template_param)

response = client.send_sms(request)
print(response)

request_id = response.body.request_id
print(request_id)