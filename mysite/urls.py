#!/usr/bin/env python
#_*_ coding:utf-8 _*_

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Blog
    url(r"^$", views.index, name="index"),
    url(r"^index/$", views.index, name="index"),
    url(r"^blog_show_lists/$", views.blog_show_lists, name="blog_show_lists"),
    url(r"^blog_show_article/(?P<article_id>[0-9]+)$", views.blog_show_article, name="blog_show_article"),
    url(r"^blog_add_page/$", views.blog_add_page, name="blog_add_page"),
    url(r"^blog_edit_page/(?P<article_id>[0-9]+)$", views.blog_edit_page, name="blog_edit_page"),
    url(r"^blog_edit_action/$", views.blog_edit_action, name="blog_edit_action"),
    url(r"^blog_del_page/(?P<article_id>[0-9]+)$", views.blog_del_page, name="blog_del_page"),


]
