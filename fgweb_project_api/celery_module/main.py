from celery import Celery
import os, django
# 引入django运行环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fgweb_project_api.settings.dev')
django.setup()

app = Celery("fuguang_web")
# 加载配置文件,表示当前celery应用,加载当前目录下的配置
app.config_from_object('celery_module.settings')

# 加载初始化任务
app.autodiscover_tasks(['celery_module.sms'])

# 启动任务