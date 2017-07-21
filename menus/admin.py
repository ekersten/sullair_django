from django.contrib import admin
from menus.models import MenuItem
from mptt.admin import DraggableMPTTAdmin
from mptt.admin import TreeRelatedFieldListFilter


class MenuItemAdmin(DraggableMPTTAdmin):
    related_lookup_fields = {
        'generic': [
            ['content_type', 'object_id']
        ],
    }
    list_display = (
        'tree_actions',
        'indented_title',
        'slug',
        'is_root'
    )
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )


admin.site.register(MenuItem, MenuItemAdmin)
