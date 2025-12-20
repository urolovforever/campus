from django.shortcuts import render
from programs.models import Program
from news.models import News
from events.models import Event
from team.models import TeamMember


def home(request):
    """Home page view with all sections"""
    context = {
        'programs': Program.objects.filter(is_active=True)[:4],
        'news': News.objects.filter(is_published=True)[:3],
        'events': Event.objects.filter(is_active=True)[:3],
        'team_members': TeamMember.objects.filter(is_active=True)[:4],
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    return render(request, 'about.html')
