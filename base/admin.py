from django.contrib import admin
from base.models import filter_table

# Register your models here.
admin.site.register(filter_table)


class FilterTable(admin.ModelAdmin):
    fields = ('location', 'price', 'rooms', 'parking', 'metr')
    list_display = ('location', 'price', 'rooms', 'parking', 'metr')
    list_filter = ('price', 'rooms', 'parking', 'metr', 'location')
    search_fields = ('location', 'price', 'rooms', 'parking', 'metr')
    empty_value_display = '-empty-'
    date_hierarchy = 'location'
