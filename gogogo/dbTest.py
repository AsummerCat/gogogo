# -*- coding: utf-8 -*-
import sys

from django.http import HttpResponse
from django.shortcuts import render
from gogogo.models import *

'''
查询全部数据
'''


def findAllDb(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Account.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Account.objects.filter(user_id=1)

    # 获取单个对象
    try:
        response3 = Account.objects.get(user_id=108)
    except:
        sys.stderr.write('当前user_id 不存在!\n')

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Account.objects.order_by('money')[0:2]

    # 数据排序
    response5 = Account.objects.order_by("user_id")

    # 上面的方法可以连锁使用
    response6 = Account.objects.filter(money=1111).order_by("user_id")
    response = ''
    # 输出所有数据
    for i in list:
        print(i.user_id, i.money)
        response += str(i.user_id) + '--->' + str(i.money) + '<br/>'

    return HttpResponse("<p>" + response + "</p>")


'''
添加数据
'''


def addAccount(request):
    test1 = Account(money=100)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


'''
更新数据
'''
def updateAccount(request):
    test1 = Account.objects.get(user_id=107)
    test1.money = 10086
    test1.save()
# 另外一种方式
# Test.objects.filter(id=1).update(name='Google')

# 修改所有的列
# Test.objects.all().update(name='Google')
    return HttpResponse("<p>修改成功</p>")

'''
删除数据
'''
def delAccount(request):
    # 删除符合条件的对象
    test1=Account.objects.filter(money=1111.0)
    test1.delete()
    # 删除单对象
    # test1 = Test.objects.get(id=1)
    # test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")


