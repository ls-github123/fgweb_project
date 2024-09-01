from ..main import app
from fgweb_project_api.settings.utils.aliyun_sms_server import send_sms

# 从main中导入celery对象 
@app.task(name="send_message")
def send_message(phone_number, template_param):
    print('--验证码短信发送任务被执行--')
    res = send_sms(phone_number, template_param)
    return res