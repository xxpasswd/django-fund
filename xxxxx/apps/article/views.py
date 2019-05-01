from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from .models import Article
# Create your views here.


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.values_list('id', 'title')
        return render(request, 'article.html', {'articles': articles})

    def post(self, request):
        return render(request, 'article_add.html')


class ArticleAddView(View):
    def get(self, request):
        return render(request, 'article_add.html')

    def post(self, request):
        title = request.POST.get('title', 'test')
        content = request.POST.get('content')
        a = Article.objects.create(title=title, content=content)
        return redirect(reverse('article:detail', args=(a.id,)))


class ArticleDetailView(View):
    def get(self, request, id):
        a = Article.objects.get(pk=id)
        return render(request, 'article_detail.html', {'article': a})


class ArticleModifyView(View):
    def get(self, request, id):
        a = Article.objects.get(pk=id)
        return render(request, 'article_modify.html', {'article': a})

    def post(self, request, id):
        a = Article.objects.get(pk=id)
        title = request.POST.get('title', 'test')
        content = request.POST.get('content')
        a.title = title
        a.content = content
        a.save()
        return redirect(reverse('article:detail', args=(a.id,)))
