from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Event
from . import translation  # noqa: F401 - Import to register translations


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ('title', 'event_date', 'event_time', 'location', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured', 'event_date')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_active', 'is_featured')
    date_hierarchy = 'event_date'
    ordering = ('event_date', 'event_time')
