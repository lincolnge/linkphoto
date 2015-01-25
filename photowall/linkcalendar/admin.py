from django.contrib import admin
from photowall.linkcalendar.models import CalType, EventName, Calendar


class EventNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'cal_type', 'counts', 'url')
    list_filter = ('name',)
    ordering = ('name',)
    fields = ('name', 'cal_type', 'counts', 'url')


class CalendarAdmin(admin.ModelAdmin):

    def get_cc_root_only(self, obj):
        if self.username == "admin":
            return obj.user
        return self.username

    def changelist_view(self, request, extra_context=None):
        self.username = request.user.username
        return super(CalendarAdmin, self).changelist_view(request, extra_context=extra_context)

    def display_resort(self, request):
        if request.user.is_superuser:
            resort_list = ['title', 'user', 'start']
        else:
            resort_list = ['title', 'start']
        return resort_list

    list_display = ('title', 'get_cc_root_only', 'start', 'end', 'allDay')
    # list_display = ['display_resort']
    list_filter = ('start',)
    ordering = ('-start',)
    fields = ('title', 'user', 'start', 'end', 'allDay')

admin.site.register(CalType)
admin.site.register(EventName, EventNameAdmin)
admin.site.register(Calendar, CalendarAdmin)
