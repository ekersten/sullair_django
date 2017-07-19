from django.contrib import admin
from genericadmin.admin import GenericAdminModelAdmin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from menus.models import Menu, MenuItem
from mptt.admin import DraggableMPTTAdmin


# admin.site.register(MenuItem, MenuItemAdmin)


class MenuAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name',]}
    list_display = ['name', 'slug']


class MenuItemAdmin(DraggableMPTTAdmin):
    related_lookup_fields = {
        'generic': [
            ['content_type', 'object_id']
        ],
    }
    list_display = ['name', 'indented_title']
    list_filter = ['menu__slug']


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
