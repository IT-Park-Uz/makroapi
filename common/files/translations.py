from modeltranslation.translator import translator, TranslationOptions

from .models import Offerta


class OffertaTranslationOptions(TranslationOptions):
    fields = ['title',]


translator.register(Offerta, OffertaTranslationOptions)
