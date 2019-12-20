"""gogogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gogogo import helloWord, dbTest, htmlFromTest, views,entityFromSumbit

urlpatterns = [
    # 路径名称 ,路径方法,路径名称 用来反向显示
    path('admin/', admin.site.urls),
    path('hello/', helloWord.hello, name='hello'),
    path('', helloWord.index, name=''),
    path('helloHtml/', helloWord.helloHtml, name='helloHtml'),
    path('findAllDb/', dbTest.findAllDb, name='findAllDb'),
    path('addAccount/', dbTest.addAccount, name='addAccount'),
    path('updateAccount/', dbTest.updateAccount, name='updateAccount'),
    path('delAccount/', dbTest.delAccount, name='delAccount'),
    path('login/', htmlFromTest.login, name='search-form'),
    path('search/', htmlFromTest.search, name='search'),
    path('postLogin/', htmlFromTest.postLogin, name='postLogin'),
    path('redirectUrl/', htmlFromTest.redirectUrl, name='redirectUrl'),
    path('articles/<int:year>/', views.year_archive),
    path('entityFromSumbit/', entityFromSumbit.entityFromSumbit,name="entityFromSumbit"),
]
