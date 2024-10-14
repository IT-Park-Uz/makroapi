from modeltranslation.translator import translator, TranslationOptions

from .models import Toys


class ToysTranslationOptions(TranslationOptions):
    fields = ['name', 'short_description', 'description', 'role', 'facts']


translator.register(Toys, ToysTranslationOptions)
