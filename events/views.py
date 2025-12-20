from django.shortcuts import render, get_object_or_404
from .models import Event


def event_list(request):
    """List all active events"""
    events = Event.objects.filter(is_active=True)
    return render(request, 'events_list.html', {'events': events})


def event_detail(request, slug):
    """Detail view for a single event"""
    event = get_object_or_404(Event, slug=slug, is_active=True)
    return render(request, 'events_detail.html', {'event': event})
