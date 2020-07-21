from users.models import User
# from apps.users.models import User   错误的  因为我们已经告诉系统users在哪 就不用apps
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

"""
1.前端发送一个ajax请求，给后台，参数是 用户名
2.后端接受用户名
3.查询校验是否重复
4.返回相应

GET  /users/usernames/(?P<username>\w{5,20})/count/
"""
# ApiView
# GenericAPIView    列表，详细，通常与mixin连用
# ListAPIView
from rest_framework.views import APIView

"""
1.前端传递过来的数据 已经在url中校验过了
2.我们也不需要 序列化器  所以使用一级视图
"""


class RegisterUsernameCountView(APIView):

    def get(self, request, username):
        count = User.objects.filter(username=username).count();
        # 4. 返回相应
        return Response({'count': count})
