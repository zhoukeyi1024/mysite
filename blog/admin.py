#!/usr/bin/env python
#coding: utf-8

from django.contrib import admin

# Register your models here.

from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "datetime")
admin.site.register(Blog, BlogAdmin)

