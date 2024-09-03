from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from course.models import TeacherModel
# Create your views here.
class IndexViews(APIView):
    def get(self,request):
        teas = TeacherModel.objects.all()

        for ta in teas:
            # print(ta.avatar.url)
            print(ta.avatar.thumb_50x50.url)

        return Response({"message":"讲师列表","data":""})