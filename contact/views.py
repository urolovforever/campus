from django.shortcuts import render


def contact(request):
    """Contact page view"""
    return render(request, 'contact.html')
