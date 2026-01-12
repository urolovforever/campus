from modeltranslation.translator import register, TranslationOptions
from .models import Partner


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name',)
