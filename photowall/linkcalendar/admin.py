from django.contrib import admin
from photowall.linkcalendar.models import CalType, EventName, Calendar


class EventNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'cal_type', 'url')
    list_filter = ('name',)
    ordering = ('name',)
    fields = ('name', 'cal_type', 'url')


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')
    list_filter = ('start',)
    ordering = ('-start',)
    fields = ('title', 'start', 'end')

admin.site.register(CalType)
admin.site.register(EventName, EventNameAdmin)
admin.site.register(Calendar, CalendarAdmin)
