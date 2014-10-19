# coding:utf8
from django.conf.urls.defaults import *

# 日历的 url
urlpatterns = patterns('photowall.linkcalendar.views',
                       url(r'^eventname/', 'eventname'),        # 有什么事件
                       url(r'^events_json/', 'events_json'),    # 显示事件
                       url(r'^events/update/', 'updateEvent'),  # 更新事件
                       )
