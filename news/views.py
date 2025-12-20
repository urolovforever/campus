from django.shortcuts import render


def news_list(request):
    """News list view"""
    return render(request, 'news_list.html')
