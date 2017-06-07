#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(u"文章标题",max_length=32, default="no title")
    content = models.TextField(blank = True, null = True)
    #content = UEditorField(u'文章内容',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},
    #        settings={},command=None,blank=True)
    datetime = models.DateField(u"时间",auto_now = True)
    tag = models.CharField(u"文章标签",max_length=32,default="none")

    class Meta:
        verbose_name = u"我的博客"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
