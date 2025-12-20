from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import NewsCategory, News
from . import translation  # noqa: F401 - Import to register translations


@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'color')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'author', 'is_published', 'published_date')
    list_filter = ('is_published', 'category', 'published_date')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
