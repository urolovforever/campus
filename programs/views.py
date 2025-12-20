from django.shortcuts import render, get_object_or_404
from .models import Program


def program_list(request):
    """List all active programs"""
    programs = Program.objects.filter(is_active=True)
    return render(request, 'programs_list.html', {'programs': programs})


def program_detail(request, slug):
    """Detail view for a single program"""
    program = get_object_or_404(Program, slug=slug, is_active=True)
    return render(request, 'program_detail.html', {'program': program})
