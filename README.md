# fgweb_project

#### 介绍:
浮光web项目，前后端代码托管


# 共享 python venv 虚拟环境的步骤:
1. 生成依赖列表 (requirements.txt)： 在虚拟环境激活的情况下，使用 pip freeze 命令生成当前环境中安装的所有包的列表，并将其保存到 requirements.txt 文件中 (pip freeze > requirements.txt);
2. 生成一个包含所有依赖的文件(如:Django==3.2 requests==2.25.1 Pillow==8.2.0 ......);
3. 将 requirements.txt 文件共享： 你可以将 requirements.txt 文件添加到项目中并通过版本控制系统（如 Git）共享给其他人;
4. 让其他人重建相同的虚拟环境： 其他人可以根据你的 requirements.txt 文件重建虚拟环境;

# 重建虚拟环境流程:
虽然不能直接共享整个虚拟环境，但可以通过 requirements.txt文件 共享环境中的依赖，使其他人可以在他们的本地机器上重新构建相同的环境

1. 创建新的虚拟环境:(python -m venv venv);
2. 激活虚拟环境: windows(venv\Scripts\activate) Linux(source venv/bin/activate);
3. 安装 requirements.txt 文件中的依赖包:(pip install -r requirements.txt)

# celery 配置:

安装celery pip包 ==>

pip install celery
#在window中使用，需要安装 以下插件
     pip install eventlet

#window中启动celery命令:
     celery -A celery_module.main worker -l info -P eventlet -c