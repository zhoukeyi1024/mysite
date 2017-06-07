#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
-------------------------------------------------
   File Name：     forms
   Description:
   Author:        zky
   date：          2017/6/7
-------------------------------------------------
"""

from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(label=u"文章标题",
                               widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入文章标题"}))
#    content = forms.CharField(label="contents",
#                               widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入文章内容"}))
    content = forms.CharField(label=u"文章内容",
                               widget=forms.Textarea(attrs={"class":"form-control","placeholder":"请输入文章内容"}))
    #datetime = forms.DateField(label="Date",
    #                         widget=forms.TextInput(attrs={"class":"form-control","placeholder":"date helre"}))
    CHOICES = (
               ("python", "python"),
               ("django","django"),
               ("html/css", "html/css"),
               ("javascript","javascript"),
               ("ubuntu","ubuntu"),
               ("centos","centos"),
               ("windows","windows"),
               ("pfsense","pfsense"),
               ("others","others")
             )
    tag = forms.CharField(label=u"文章标签",
                            widget=forms.Select(choices=CHOICES, attrs={"class":"form-control"}))
    #tag = forms.IntegerField(label=u"文章标签",
    #                     widget=forms.Select(choices=CHOICES, attrs={"class":"form-control"}))
