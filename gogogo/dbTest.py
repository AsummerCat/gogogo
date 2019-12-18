# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from gogogo.models import *

'''
查询全部数据
'''
def findAllDb(request):
    list = Account.objects.all()
    for a in list:
      print( a.user_id,"---->",a.money)

    return HttpResponse("查询数据成功! ")
