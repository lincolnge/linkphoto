# coding:utf8

from django.shortcuts import render_to_response
from photowall.linkcalendar.models import CalType, EventName, Calendar
from django.views.decorators.csrf import csrf_exempt
# 时区问题 = =
from django.utils.timezone import utc, localtime

import json
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


# 事件
@csrf_exempt
def eventname(request):
    # tmp = EventName.objects.filter(user_id=request.user.id)
    tmp = EventName.objects.all()
    events = []

    for entry in tmp:
        id = entry.id
        name = entry.name
        cal_type = CalType.objects.get(
            id=entry.cal_type_id)
        counts = entry.counts
        url = entry.url

        json_entry = {'id': id, 'name': name,
                      'cal_type': cal_type.name, 'counts': counts, 'url': url}
        events.append(json_entry)

    return HttpResponse(json.dumps(events), content_type='application/json')


# 输出 JSON
@csrf_exempt
def events_json(request):
    tmp = Calendar.objects.filter(user_id=request.user.id)
    # tmp = Calendar.objects.all()
    events = []

    # 这种不行, 不知道为啥
    # tmpevents = {}
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

        title_id = entry.title_id
        event_info = EventName.objects.get(
            id=title_id)
        title = event_info.name
        cal_type = event_info.cal_type.name
        counts = event_info.counts
        url = event_info.url

        if entry.start:
            start = localtime(entry.start.replace(tzinfo=utc)).strftime(
                "%Y-%m-%dT%H:%M:%S")
        else:
            start = entry.start
        if entry.end:
            end = localtime(entry.end.replace(tzinfo=utc)).strftime(
                "%Y-%m-%dT%H:%M:%S")
        else:
            end = entry.end
        allDay = entry.allDay

        json_entry = {'id': id, 'title_id': title_id, 'title': title, 'cal_type': cal_type, 'counts':
                      counts, 'url': url, 'start': start, 'end': end, 'allDay': allDay}
        events.append(json_entry)

    # return render_to_response('index.html', locals())
    return HttpResponse(json.dumps(events), content_type='application/json')


@csrf_exempt
def updateEvent(request):
    print request.method
    if request.method == 'POST':
        if request.user.is_authenticated():
            # Do something for authenticated users.
            print 'y'
            print request.user.id  # 用户 id
            title_id = request.POST['title_id']

            start = datetime.strptime(
                request.POST['start'],
                "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S")

            event = Calendar(
                user_id=request.user.id, title_id=title_id, start=start)

            event.save()
        else:
            # Do something for anonymous users.
            print 'n'
    return HttpResponse()
