# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    article = models.Article.objects.get(pk=3)
    return render(request, 'testApp/index.html', {'article': article})

# def index(request):
#     return HttpResponse('hello')