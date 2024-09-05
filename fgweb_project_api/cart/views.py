from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from course.models import CourseModel
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection

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