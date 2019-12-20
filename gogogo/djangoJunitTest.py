# -*- coding: utf-8 -*-
'''
django单元测试
'''

'''
简单测试例子
'''
from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')


'''
用代码访问网址的方法
'''
from django.test import Client


def test():
    c = Client()
    response = c.post('/login/', {'username': 'john', 'password': 'smith'})
    print(response.status_code)
    response = c.get('/customer/details/')
    print(response.content)
    '''
    默认情况下CSRF检查是被禁用的，如果测试需要，可以用下面的方法：
    '''
    csrf_client = Client(enforce_csrf_checks=True)
    '''
    指定浏览USER-AGENT
    '''
    c = Client(HTTP_USER_AGENT='Mozilla/5.0')
    '''
    模拟POST请求上传文件
    '''
    with open('wishlist.doc') as fp:
        c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})

    '''
    测试页面返回状态
    '''
    from django.test import TestCase
    class SimpleTest(TestCase):
        def test_details(self):
            response = self.client.get('/customer/details/')
            self.assertEqual(response.status_code, 200)

        def test_index(self):
            response = self.client.get('/customer/index/')
            self.assertEqual(response.status_code, 200)