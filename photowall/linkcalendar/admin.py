from django.contrib import admin
from photowall.linkcalendar.models import Calendar

# class CalendarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'publisher', 'publication_date')
#     list_filter = ('publication_date',)
#     date_hierarchy = 'publication_date'
#     ordering = ('-publication_date',)
#     # fields = ('title', 'authors', 'publisher')
#     filter_horizontal = ('authors',)
#     raw_id_fields = ('publisher',)

# admin.site.register(Publisher)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Calendar)