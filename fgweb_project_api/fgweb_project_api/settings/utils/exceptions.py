# DRF 异常处理器
from rest_framework.views import exception_handler # 异常分发
from django.db import DataError # 数据库异常
from rest_framework import status # 状态码返回
from rest_framework.response import Response
import logging

logger = logging.getLogger('django') # 日志处理器

def costom_exception_handler(exc,context):
    # 自定义异常处理
    # exc:exception 异常类
    # context:上下文
    # return: response 响应结果对象
    
    # 调用DRF框架原生异常处理方法
    response = exception_handler(exc, context)
    if response is None:
        # 报错视图
        view = context['view']
        if isinstance(exc, DataError):
            # 数据库操作异常
            logger.error("[%s] %s" % (view, exc))
            response = Response({"message":"服务器内部错误...."}, status = status.HTTP_507_INSUFFICIENT_STORAGE)
        if isinstance(exc, ZeroDivisionError):
            logger.error("[%s] %s" % (view, exc))
            # 需要展示重定向页面，还是返回具体状态码，实际业务需求决定
            response = Response({"message":"服务器错误.....", "code":"10005"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    return response