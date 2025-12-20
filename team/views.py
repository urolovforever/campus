from django.shortcuts import render
from .models import TeamMember


def team_list(request):
    """View to display list of all active team members"""
    team_members = TeamMember.objects.filter(is_active=True)
    context = {
        'team_members': team_members
    }
    return render(request, 'team_list.html', context)
