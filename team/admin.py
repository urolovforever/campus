from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import TeamMember
from . import translation  # noqa: F401 - Import to register translations


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('name', 'position', 'email', 'is_active', 'order')
    list_filter = ('is_active', 'joined_date')
    search_fields = ('name', 'position', 'bio', 'email')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'name')
