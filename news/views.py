from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    """List all published news articles"""
    news_list = News.objects.filter(is_published=True)
    return render(request, 'news_list.html', {'news_list': news_list})


def news_detail(request, slug):
    """Detail view for a single news article"""
    news = get_object_or_404(News, slug=slug, is_published=True)
    return render(request, 'news_detail.html', {'news': news})
