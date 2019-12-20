# -*- coding: utf-8 -*
# 表单转换实体后提交
from django import forms

'''
dto 映射的实体
'''


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
