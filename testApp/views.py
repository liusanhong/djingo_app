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


def article_edit_page(request):
    return render(request, 'testApp/article_edit_page.html')


def article_edit_page_action(request):
    title = request.POST.get('title', 'default title')
    content = request.POST.get('content', 'default content')
    models.Article.objects.create(title=title, content=content)

    articles = models.Article.objects.all()
    return render(request, 'testApp/index.html', {'articles': articles})


# def index(request):
#     return HttpResponse('hello')