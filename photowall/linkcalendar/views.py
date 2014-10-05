# coding:utf8

from django.shortcuts import render_to_response
from photowall.linkcalendar.models import Calendar

import json
from django.http import HttpResponse

# Create your views here.

def my_homepage_view(request):
    return render_to_response('index.html')

# 输出 JSON
def events_json(request):
    tmp = Calendar.objects.all()
    events = []
    tmpevents = {}

    for x in xrange(0, len(tmp)):
        tmpevents['cal_type'] = tmp[x].cal_type
        tmpevents['title'] = tmp[x].title
        if tmp[x].start:
            tmpevents['start'] = tmp[x].start.strftime("%Y-%m-%dT%H:%M:%S")
        if tmp[x].end:
            tmpevents['end'] = tmp[x].end.strftime("%Y-%m-%dT%H:%M:%S")
        tmpevents['allDay'] = tmp[x].allDay
        tmpevents['url'] = tmp[x].url

        events.append(tmpevents)

    # Or 这种写法
    # for entry in tmp:
    #     id = entry.id
    #     cal_type = entry.cal_type
    #     title = entry.cal_title
    #     start = entry.start.strftime("%Y-%m-%d %H:%M:%S")
    #     allDay = entry.allDay

    #     json_entry = {'id':id, 'start':start, 'allDay':allDay, 'title': title}
    #     events.append(json_entry)

    # return render_to_response('index.html', locals())
    return HttpResponse(json.dumps(events), content_type='application/json')
