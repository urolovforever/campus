from django.shortcuts import render


def home(request):
    """Home page view"""
    return render(request, 'home.html')


def about(request):
    """About page view"""
    return render(request, 'about.html')
