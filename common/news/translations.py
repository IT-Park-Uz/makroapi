from modeltranslation.translator import translator, TranslationOptions

from .models import News, Region, District, Location


class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


translator.register(News, NewsTranslationOptions)


class RegionTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(Region, RegionTranslationOptions)


class DistrictTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(District, DistrictTranslationOptions)


class LocationTranslationOptions(TranslationOptions):
    fields = ['title', 'address']


translator.register(Location, LocationTranslationOptions)
