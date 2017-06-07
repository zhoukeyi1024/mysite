#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render, redirect
from django.contrib import messages

from  .models import  Blog
from  .forms import BlogForm


# Create your views here.


def index(request):
    articles = Blog.objects.all()
    return render(request, "index.html",{"articles": articles})


def blog_add_page(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            print "---------- Blog form valid OK"
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            tag = form.cleaned_data["tag"]
            #datetime = form.cleaned_data["datetime"]
            print title, content, tag
            Blog.objects.create(title=title, content=content, tag=tag)   #write data to db
            messages.info(request, 'Add done!', extra_tags="alert alert-info")
            #blogs = Blog.objects.all()
            #return render(request, "blog_show_lists.html", {"blogs":blogs})    #Refresh webpage will cause post again
            return  redirect("/index/")           #redirect webpage solve problem "post again"
    else:
        print "5555555555555"
        form = BlogForm()
    return render(request, "blog_add_page.html", {"form": form})


def blog_edit_page(request, article_id):
    article = Blog.objects.get(pk=article_id)
    print "blog edit page:", article_id
    #title = request.POST.get("title", "TITLe")
    #content = request.POST.get("content", "CONTENT")
    #datetime = request.POST.get("datetime", "DATETIME")
    #print title, content, datetime
    # 添加数据到数据库
    #Blog.objects.create(title=title, content=content, datetime=datetime)
    return render(request, "blog_edit_page.html", {"article": article})


def blog_edit_action(request):
    id = request.POST.get("article_id","99")
    print "blog edit action on article id:",id
    title = request.POST.get("title", "TITLE")
    content = request.POST.get("content", "CONTENT")
    tag = request.POST.get("tag", "TAG")
    datetime = request.POST.get("datetime", "2222-2-22")
    print id,title, content,tag, datetime
    #write data to db
    article = Blog.objects.get(pk=id)
    article.title = title
    article.content = content
    article.tag = tag
    article.datetime = datetime
    article.save()
    print "article edit done! "
    messages.info(request, '修改成功!', extra_tags="alert alert-info")
    return render(request, "blog_show_article.html", {"article": article})
    #return  redirect("/blog_show_lists/")


def blog_show_lists(request):
    blogs = Blog.objects.all()
    return render(request, "blog_show_lists.html", {"blogs": blogs})

def blog_del_page(request, article_id):
    #id = request.GET("blog_id")
    print "del id:", article_id
    Blog.objects.filter(pk=article_id).delete()
    articles = Blog.objects.all()
    messages.info(request, '删除完成!', extra_tags="alert alert-info")
    return render(request, "index.html", {"articles": articles})


def blog_show_article(request, article_id):
    print "find article_id:",article_id
    article = Blog.objects.get(pk=article_id)
    return render(request, "blog_show_article.html", {"article": article})