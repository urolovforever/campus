from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Program
from . import translation  # noqa: F401 - Import to register translations


@admin.register(Program)
class ProgramAdmin(TranslationAdmin):
    list_display = ('title', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order', 'is_active')
    ordering = ('order', '-created_at')
