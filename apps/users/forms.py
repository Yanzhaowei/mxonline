# -*-coding: utf-8 -＊-
__author__ = 'zyw'
__date__ = '18-2-18 下午3:44'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)