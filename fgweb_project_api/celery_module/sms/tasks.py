from ..main import app
from fgweb_project_api.settings.utils.aliyun_sms_server import send_sms

# 从main中导入celery对象 
@app.task(name="send_message")
def send_message(phone_number, template_param):
    try:
        # 发送短信的代码
        return {'status': 'success', 'message': '短信发送成功'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}