from django.contrib import admin
from photowall.linkcalendar.models import Calendar

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'cal_type', 'start', 'end', 'url')
    list_filter = ('start',)
    ordering = ('-start',)
    fields = ('title', 'cal_type', 'start', 'end', 'url')

admin.site.register(Calendar, CalendarAdmin)