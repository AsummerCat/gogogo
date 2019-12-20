# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from gogogo import entityFromDto


def entityFromSumbit(request):
    if request.method == 'POST':  # 当提交表单时

        form = entityFromDto.AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = entityFromDto.AddForm()
    return render(request, 'entityFromSumbit.html', {'form': form})
