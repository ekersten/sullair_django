from django.shortcuts import render, get_object_or_404

from website.models import Page, ProductCategory


# Create your views here.
def page(request, slug):

    page_obj = get_object_or_404(Page, full_slug=slug)

    context = {
        'slug': slug,
        'page': page_obj
    }

    return render(request, 'website/page.html', context)

def category(request, slug):
    category_obj = get_object_or_404(ProductCategory, full_slug=slug)

    context = {
        'slug': slug,
        'item': category_obj
    }

    return render(request, 'website/product_category.html', context)