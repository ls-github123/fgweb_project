from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from course.models import CourseModel
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection

# 获取购物车中勾选的商品列表
class CartToOrderViews(APIView):
    permission_classes = [IsAuthenticated] # 配置访问权限 仅允许已认证用户访问
    
    def get(self, request):
        user_id = request.user.id
        # 从redis中根据用户id,获取当前用户所有数据
        redis = get_redis_connection('cart')
        
        cart_hash = redis.hgetall(f"cart_{user_id}")
        if len(cart_hash) < 1:
            return Response({"message":"购物车中没有添加任何课程信息..."}, status=status.HTTP_204_NO_CONTENT)
        # 获取购物车中的数据   购物车中的数据
        cart = [(int(key.decode()),bool(int(value.decode()))) for key,value in cart_hash.items()]
            # [(1,True),(2,True)]
        # 数据，判断
        # 获取选中课程id列表
        course_id_list = [i[0] for i in cart if i[1]==True]
        # 根据选中课程id列表，获取课程详细信息
        course_list = CourseModel.objects.filter(id__in=course_id_list,is_deleted=False,is_show=True)
        # 创建空列表，用于存放课程精简信息（课程列表）
        data = []

        for course in course_list:
            data.append({
                "id":course.id,
                "name":course.name,
                "course_cover":"http://127.0.0.1:8000"+course.course_cover.url,
                "price":course.price,
                "discount":course.discount,
                "course_type":course.course_type,
                "credit":course.credit,
            })
        return Response({"message":"获取购物车选中商品成功",'cart':data})

class CartViews(APIView):
    # 配置，访问视图接口的用户权限
    permission_classes = [IsAuthenticated,]
    # drf配置了用户校验的操作
    
    def get(self,request):
        # 获取购物车
        user_id = request.user.id
        redis = get_redis_connection('cart')
        cart_hash = redis.hgetall(f"cart_{user_id}")
        print(cart_hash)
        # cart_hash = {
        #     b'1':b'1',
        #     b'2':b'1',
        # }
        # 根据redis返回数量,判读是否有数据存在redis中
        if len(cart_hash)<1:
            return Response({'message': '没有数据'})

        # 有数据,将redis中获取到的数据,转成python中可以使用的数据类型
        cart = [(int(key.decode()),bool(value.decode())) for key,value in cart_hash.items()]
        # [(2,True),(3,False),,,,,,,,]
        # 获取redis中所有的课程id,
        course_id_list = [i[0] for i in cart]
        # 1,2,14,15,16
        # 数据数据库中查询课程数据,
        course_list = CourseModel.objects.filter(id__in=course_id_list,is_deleted=False,is_show=True)

        data = []

        for course in course_list:
            data.append(
                {
                    "id":course.id,
                    "name":course.name,
                    "course_cover":"http://127.0.0.1:8000"+course.course_cover.url,
                    "price":float(course.price),
                    "discount":course.discount,
                    "course_type":course.course_type,
                    "credit":course.credit,
                    # 勾选状态,判断在redis中是否存在,
                    # redis中存储的值,是否是选中状态
                    # 课程id和redis结果比较
                    "selected": (str(course.id).encode()) in cart_hash and
                                cart_hash[str(course.id).encode()].decode() == "1"
                }
            )
        return Response({'message':'获取购物车数据成功',"cart":data})
    
    
    def post(self,request):
        user_id = request.user.id
        # 获取课程id
        course_id = request.data.get('course_id')
        # 默认选中
        selected = 1

        # 判断课程是否存在
        try:
            CourseModel.objects.get(is_deleted=False,is_show=True,id=course_id)
            # userid:{
            #     课程id：1，
            #     课程id:1,
            # }
            redis = get_redis_connection('cart')

            redis.hset(f"cart_{user_id}",course_id,selected)

            cart_total = redis.hlen(f"cart_{user_id}")

            return Response({'message': '购物车添加成功','cart_total':cart_total},
                        status=status.HTTP_200_OK)

        except CourseModel.DoesNotExist:
            print('课程不存在，添加购物车失败，请刷新课程信息......')
            return Response({'message':'课程不存在，添加购物车失败，请刷新课程信息......'},status=status.HTTP_400_BAD_REQUEST)
        
    # 选定状态改变
    def patch(self, request):
        user_id = request.user.id
        # 课程ID
        coruse_id = request.data.get('course_id', None)
        # 获取前端课程选中状态
        selected = request.data.get("selected", True)
        redis = get_redis_connection('cart')
        # 判断课程是否存在
        try:
            CourseModel.objects.get(id=coruse_id, is_deleted=False, is_show=True)
        except CourseModel.DoesNotExist:
            print('操作课程不存在')
            # 删除数据库中的数据
            redis.hdel(f"cart_{user_id}", coruse_id)
            return Response({"message":"当前课程不存在,或已下架"}, status=status.HTTP_400_BAD_REQUEST)
        print('修改课程选中状态......')
        redis.hset(f"cart_{user_id}", coruse_id, selected)
        
        # hset(key, 域, 值)
        return Response({"message":"状态修改成功"}, status=status.HTTP_200_OK)
    
    # 购物车列表全选/删除
    def put(self, request):
        # 用户id 全选状态/未选中
        user_id = request.user.id
        selected = int(request.data.get('selected'))
        redis = get_redis_connection('cart')
        cart_hash = redis.hgetall(f"cart_{user_id}")
        # 判断当前用户，是否存在购买课程
        if len(cart_hash) < 1:
            return Response({"message":"购物车没有数据,请先添加需要购买的课程"}, status=status.HTTP_200_OK)
        
        # 获取购物车中所有课程 id
        cart_list = [int(c.decode()) for c in cart_hash]
        # 开启管道 将redis多个命令 同时打包发送至redis数据库 减少频繁访问的网络压力
        pipe = redis.pipeline()
        pipe.multi()
        for i in cart_list:
            pipe.hset(f"cart_{user_id}", i, selected)
        # 执行管道提交
        pipe.execute()
        return Response({"message":"全选状态修改成功..."}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        # 课程id以何种方式传递 id 路径 查询参数
        course_id = request.query_params.get('course_id')
        user_id = request.user.id
        redis = get_redis_connection('cart')
        redis.hdel(f"cart_{user_id}", course_id)
        return Response({"message":"购物车课程删除成功..."}, status=status.HTTP_200_OK)