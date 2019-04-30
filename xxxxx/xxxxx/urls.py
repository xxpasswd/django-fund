"""xxxxx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('reset_password', ResetView.as_view(), name='reset_password'),
    path('get_token/<str:token>', GetTokenView.as_view(), name='get_token'),
    path(r'captcha/', include('captcha.urls')),

    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', RedirectView.as_view(url='fund/', permanent=True)),
    path('fund/', include(('fund.urls', 'fund'), namespace='fund')),

    path('article/', include(('article.urls', 'article'), namespace='article'))
]
