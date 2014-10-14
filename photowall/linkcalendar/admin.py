from django.contrib import admin
from photowall.linkcalendar.models import EventName, Calendar


class EventNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cal_type', 'url')
    list_filter = ('title',)
    ordering = ('title',)
    fields = ('title', 'cal_type', 'url')


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'cal_type', 'start', 'end', 'url')
    list_filter = ('start',)
    ordering = ('-start',)
    fields = ('title', 'cal_type', 'start', 'end', 'url')

admin.site.register(EventName, EventNameAdmin)
admin.site.register(Calendar, CalendarAdmin)
