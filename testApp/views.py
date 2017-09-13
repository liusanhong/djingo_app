# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'testApp/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'testApp/article_page.html', {'article': article})


def article_edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'testApp/article_edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'testApp/article_edit_page.html', {'article': article})


def article_edit_page_action(request):
    title = request.POST.get('title', 'default title')
    content = request.POST.get('content', 'default content')
    article_id = request.POST.get('article_id_hidden', '0')
    if article_id == '0':
        # 新建博客
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'testApp/index.html', {'articles': articles})
    # 修改博客
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'testApp/article_page.html', {'article': article})


# def index(request):
#     return HttpResponse('hello')