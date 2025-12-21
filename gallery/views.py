from django.shortcuts import render
from .models import Gallery


def gallery_list(request):
    """Gallery page view displaying all gallery images"""
    category = request.GET.get('category')

    if category:
        gallery_images = Gallery.objects.filter(category=category)
    else:
        gallery_images = Gallery.objects.all()

    categories = Gallery.CATEGORY_CHOICES

    context = {
        'gallery_images': gallery_images,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery.html', context)
