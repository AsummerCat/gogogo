# -*- coding: utf-8 -*-
#  html表单提交
from django.http import HttpResponse
from django.shortcuts import render, redirect


# GET表单
def login(request):
    return render(request, 'search_form.html', {})


# GET接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


# post表单
def postLogin(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']

    print(request.META.get("REMOTE_ADDR"))

    return render(request, "post.html", ctx)

# 重定向 需要导入 from django.shortcuts import  redirect

def redirectUrl(request):
    return redirect("http://www.baidu.com")