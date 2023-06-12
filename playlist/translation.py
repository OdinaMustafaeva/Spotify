from modeltranslation.translator import translator, TranslationOptions
from .models import Playlist


class BlogTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Playlist, BlogTranslationOptions)
