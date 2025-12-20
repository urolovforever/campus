from django.shortcuts import render
from .models import TeamMember


def team_list(request):
    """List all active team members"""
    team_members = TeamMember.objects.filter(is_active=True)
    return render(request, 'team_list.html', {'team_members': team_members})
