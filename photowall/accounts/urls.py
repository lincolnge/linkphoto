# coding:utf8
from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

# 帐号系统的 url
urlpatterns = patterns('photowall.accounts.views',
                       url(r'^login/', login),
                       # url(r'^logout/', logout),
                       url(r'^logout/', 'logout'),
                       url(r'^register/', 'register'),  # 注册
                       url(r'^profile/', 'profile'),  # 个人页面
                       url(r'^password/', 'password'),  # 修改密码
                       )
