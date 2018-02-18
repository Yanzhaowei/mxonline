# coding: utf-8
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import UserProfile
# Create your views here.


# 使用邮箱登录
# 自定义，要在settings中配置
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def users_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_pwd = request.POST.get('password')
        user = authenticate(username=user_name, password=user_pwd )
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            return render(request, 'login.html', {'msg': '用户未激活！'})
        return render(request, 'login.html', {'msg': '用户名或者密码错误！'})

    else:
        return render(request, 'login.html')