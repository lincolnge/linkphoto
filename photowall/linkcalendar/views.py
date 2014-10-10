# coding:utf8

from django.shortcuts import render_to_response
from photowall.linkcalendar.models import Calendar
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


def my_homepage_view(request):
    return render_to_response('index.html')

# 输出 JSON


def events_json(request):
    tmp = Calendar.objects.all()
    events = []
    tmpevents = {}

    end_events = []

    # 这种不行, 不知道为啥
    # for x in xrange(0, len(tmp)):
    #     tmpevents['cal_type'] = tmp[x].cal_type
    #     tmpevents['title'] = tmp[x].title
    #     if tmp[x].start:
    #         tmpevents['start'] = tmp[x].start.strftime("%Y-%m-%dT%H:%M:%S")
    #     if tmp[x].end:
    #         tmpevents['end'] = tmp[x].end.strftime("%Y-%m-%dT%H:%M:%S")
    #     tmpevents['allDay'] = tmp[x].allDay
    #     tmpevents['url'] = tmp[x].url

    #     events.append(tmpevents)
    #     print events

    for entry in tmp:
        id = entry.id
        cal_type = entry.cal_type
        title = entry.title
        if entry.start:
            start = entry.start.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            start = entry.start
        if entry.end:
            end = entry.end.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            end = entry.end
        allDay = entry.allDay
        url = entry.url

        json_entry = {'id': id, 'title': title, 'cal_type': cal_type,
                      'start': start, 'end': end, 'allDay': allDay, 'url': url}
        events.append(json_entry)

    # return render_to_response('index.html', locals())
    return HttpResponse(json.dumps(events), content_type='application/json')


@csrf_exempt
def updateEvent(request):
    print request.method
    if request.method == 'POST':
        event = Calendar(title=request.POST['title'], start=datetime.strptime(
            request.POST['start'], "%Y-%m-%dT%H:%M:%S.%fZ"))
        event.save()
    return HttpResponse()
