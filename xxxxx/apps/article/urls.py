# coding: utf-8
from django.urls import path, include

from .views import ArticleView, ArticleAddView, ArticleDetailView


urlpatterns = [
    path('', ArticleView.as_view(), name='index'),
    path('add/', ArticleAddView.as_view(), name='add'),
    path('<int:id>/', ArticleDetailView.as_view(), name='detail')
    ]