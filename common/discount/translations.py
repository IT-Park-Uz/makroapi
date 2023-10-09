from modeltranslation.translator import translator, TranslationOptions

from .models import Discount


class DiscountTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'titleFile']


translator.register(Discount, DiscountTranslationOptions)
