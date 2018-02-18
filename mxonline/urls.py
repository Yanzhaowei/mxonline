# coding: utf-8
"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from django.views.generic import TemplateView

from users.views import LoginView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 用户中心 URL 配置
    url(r'^users/', include('users.urls', namespace='users')),
    # index
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # 基于类的登录函数
    url(r'login/$', LoginView.as_view(), name='login'),
]
