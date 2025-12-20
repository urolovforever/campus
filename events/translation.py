from modeltranslation.translator import translator, TranslationOptions
from .models import Event


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description', 'location')


translator.register(Event, EventTranslationOptions)
