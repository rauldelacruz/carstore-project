from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width = "40" style="border-radius: 50px" />'.format(object.photo.url))

    thumbnail.short_description = 'Pic'

    list_display = ('thumbnail','id', 'first_name', 'last_name', 'role', 'created_date')
    list_display_links = ('thumbnail', 'id', 'first_name')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)



admin.site.register(TeamMember, TeamAdmin)
