# coding: utf-8
from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=3)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    captcha = CaptchaField()

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError('两次密码不一致', code='not equal')
