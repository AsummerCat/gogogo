# -*- coding: utf-8 -*-
import datetime
import time

from django.http import HttpResponse

"""
直接返回字符串
"""


def hello(request):
    return HttpResponse("hello world ! ")


from django.shortcuts import render

'''
这边使用模板
'''


def helloHtml(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['athlete_list'] = ['abcd', 786, 2.23, 'runoob', 70.2]
    context['testNumber'] = 1
    context['pub_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    context['create_time'] = datetime.datetime.now()

    return render(request, 'hello.html', context)


def index(request):
    context = {}
    return render(request, 'test111.html', context)

