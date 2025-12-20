from django.shortcuts import render


def program_list(request):
    """Programs list view"""
    return render(request, 'programs_list.html')
