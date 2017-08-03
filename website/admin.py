from django.contrib import admin
from django import forms

from mptt.admin import DraggableMPTTAdmin

from tinymce.widgets import TinyMCE

from website.models import BranchType, BranchCategory, Branch
from website.models import CompanyCategory
from website.models import Contact
from website.models import Page
from website.models import ProductProperty, ProductCategory, ProductPropertyValue, Product


class ProductCategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ['name']}


class PageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'theme': 'advanced', 'height': 480}))

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ['title']}
    form = PageForm


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
