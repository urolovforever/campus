from modeltranslation.translator import translator, TranslationOptions
from .models import TeamMember


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('position', 'bio', 'short_bio')


translator.register(TeamMember, TeamMemberTranslationOptions)
