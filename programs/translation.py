from modeltranslation.translator import translator, TranslationOptions
from .models import Program


class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description', 'impact_stat')


translator.register(Program, ProgramTranslationOptions)
