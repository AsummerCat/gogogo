# -*- coding: utf-8 -*-
from django import http
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

'''
黑名单拦截器
'''
class BlockedIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in getattr(settings, "BLOCKED_IPS", []):
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')
        else:
            print("并未加入黑名单")
