from modeltranslation.translator import translator, TranslationOptions

from .models import Discount, DiscountFiles


class DiscountTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'titleFile']


translator.register(Discount, DiscountTranslationOptions)


class DiscountFilesTranslationOptions(TranslationOptions):
    fields = ['titleFile']


translator.register(DiscountFiles, DiscountFilesTranslationOptions)
