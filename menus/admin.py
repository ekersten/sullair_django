from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from menus.models import MenuItem


# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    class Media:
        js = ('menus/js/menus-admin.js',)

admin.site.register(MenuItem, MenuItemAdmin)
