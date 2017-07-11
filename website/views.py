from django.shortcuts import render, get_object_or_404

from website.models import Page


# Create your views here.
def page(request, slug):

    page_obj = get_object_or_404(Page, full_slug=slug)

    context = {
        'slug': slug,
        'page': page_obj
    }



    return render(request, 'website/index.html', context)