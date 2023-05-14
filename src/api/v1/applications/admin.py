from django.contrib import admin

# Register your models here.
from .models import Application, Job, JobHeader


class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('id', 'job', 'user')
    list_display_links = ('job', )
    search_fields = ('job', 'user')
    list_filter = ('job', 'user')


admin.site.register(Application, ApplicationAdmin)


class JobAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "type")
    list_display_links = ("id", "name", "type")
    search_fields = ("name", "type")
    list_filter = ("name", "type")


admin.site.register(Job, JobAdmin)


class JobHeaderAdmin(admin.ModelAdmin):
    list_display = ("id", "rich_title_text", "rich_subtitle_text", "job")
    list_display_links = ("id", "rich_title_text", "rich_subtitle_text", "job")
    search_fields = ("rich_title_text", "rich_subtitle_text", "job")
    list_filter = ("rich_title_text", "rich_subtitle_text", "job")


admin.site.register(JobHeader, JobHeaderAdmin)
