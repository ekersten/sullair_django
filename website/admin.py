from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from jet.admin import CompactInline

from website.models import BranchType, BranchCategory, Branch
from website.models import CompanyCategory
from website.models import Contact
from website.models import Page
from website.models import ProductProperty, ProductCategory, ProductPropertyValue, Product


class ProductCategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ['name']}


class PageAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ['title']}

class ProductPropertyValueInline(admin.TabularInline):
    model = ProductPropertyValue


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    inlines = [
        ProductPropertyValueInline
    ]


admin.site.register(BranchType)
admin.site.register(BranchCategory)
admin.site.register(Branch)
admin.site.register(CompanyCategory, DraggableMPTTAdmin)
admin.site.register(Contact)
admin.site.register(Page, PageAdmin)
admin.site.register(ProductProperty)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
