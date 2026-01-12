from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(TranslationAdmin):
    list_display = ('name', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'website_url')
    list_editable = ('order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Partner Information', {
            'fields': ('name', 'logo', 'website_url')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
