from .models import Car
from django.contrib import admin
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Pic'
    list_display = ('id','thumbnail','title', 'location', 'color', 'make', 'model', 'year', 'body_style', 'fuel_type', 'created_date', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'title', 'location', 'make', 'model', 'body_style', 'fuel_type', 'transmission', 'year')
    list_filter = ('location', 'make', 'model', 'body_style', 'fuel_type', 'transmission', 'is_featured', )

admin.site.register(Car, CarAdmin)