from django.shortcuts import render


def event_list(request):
    """Events list view"""
    return render(request, 'events_list.html')
