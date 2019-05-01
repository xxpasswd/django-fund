# coding: utf-8
from django.urls import path, include
from django.views.generic import TemplateView

from .views import FundIndexView


urlpatterns = [
    path('', FundIndexView.as_view(), name='index')
    ]