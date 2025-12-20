from modeltranslation.translator import translator, TranslationOptions
from .models import NewsCategory, News


class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'content')


translator.register(NewsCategory, NewsCategoryTranslationOptions)
translator.register(News, NewsTranslationOptions)
