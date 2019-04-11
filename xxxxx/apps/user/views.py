from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View, reverse
import jwt
from django.conf import settings

from user.forms import LoginForm, RegisterForm
from utils.email_helper import send_register_email
from .models import UserProfile
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
            return None
        except Exception as e:
            return None


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                path = request.GET.get('next')
                return redirect(path)
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            UserProfile.objects.create_user(username=username, password=password)
            send_register_email('pfei_xy@sina.com', username+'注册成功！')
            return redirect('login')
        return render(request, 'register.html', {'msg': form.errors, 'form': form})


class ResetView(View):
    def get(self, request):
        return render(request, 'reset_password.html')

    def post(self, request):
        email = request.POST.get('email')
        token = jwt.encode({'a': 'b'}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        url = request.build_absolute_uri('/get_token/')
        send_register_email(email, url+token)
        return redirect('login')


class GetTokenView(View):
    def get(self, request, token):
        content = jwt.decode(token, settings.SECRET_KEY, algorithm=['HS256'])
        return HttpResponse(str(content))
