from django.contrib import admin
from photowall.linkcalendar.models import CalType, EventName, Calendar
from datetime import datetime


class EventNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'cal_type', 'counts', 'url')

    selected_fieldsets = (
        (None, {
            'fields': ('name', 'cal_type')
        }),
        ('Advanced options', {
            'fields': ('counts', 'url')
        }),
    )

    admin_fieldsets = (
        (None, {
            'fields': ('name', 'user', 'cal_type')
        }),
        ('Advanced options', {
            'fields': ('counts', 'url')
        }),
    )

    def queryset(self, request):
        qs = super(EventNameAdmin, self).queryset(request)
        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_fieldsets(self, request, obj=None):
        """
        This function would limit the fieldset for project admins.
        For project admins, we used selected_fieldsets.
        """
        if request.user.is_superuser:
            # Show me everything, for I'm root.
            # return super(EventNameAdmin, self).get_fieldsets(request, obj)
            fields = ('name', 'user', 'counts', 'cal_type', 'url')
            return self.admin_fieldsets
        else:
            # Show project admins selected fields.
            return self.selected_fieldsets

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        if not obj.counts:
            obj.counts = 0
        obj.save()


class CalendarAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(CalendarAdmin, self).queryset(request)
        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    list_display = ('title', 'user', 'start', 'end', 'allDay')
    list_filter = ('start',)
    ordering = ('-start',)

    selected_fieldsets = (
        (None, {
            'fields': ('title', 'start')
        }),
        ('Advanced options', {
            'fields': ('end', 'allDay')
        }),
    )

    admin_fieldsets = (
        (None, {
            'fields': ('title', 'user', 'start')
        }),
        ('Advanced options', {
            'fields': ('end', 'allDay')
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return self.admin_fieldsets
        else:
            return self.selected_fieldsets

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        if not obj.start:
            obj.start = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        obj.save()

admin.site.register(CalType)
admin.site.register(EventName, EventNameAdmin)
admin.site.register(Calendar, CalendarAdmin)
