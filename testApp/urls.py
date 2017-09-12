
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
    url(r'^article/edit$', views.article_edit_page, name='article_edit_page'),
    url(r'^article/edit/action$',views.article_edit_page_action, name='article_edit_page_action'),
]
