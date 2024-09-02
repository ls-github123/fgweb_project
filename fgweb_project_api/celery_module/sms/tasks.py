from ..main import app
from fgweb_project_api.settings.utils.aliyun_sms_server import send_sms
from redis.exceptions import RedisError

# 从main中导入celery对象 
@app.task(name="send_message")
def send_message(phone_number, template_param):
    try:
        # 发送短信的代码
        response = send_sms(phone_number, template_param)  # 调用短信发送函数
        if response.Code == 'OK':  # 如果短信发送成功
            return {'status': 'success', 'message': '验证码发送成功'}
        else:
            return {'status': 'error', 'message': '验证码发送失败'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}