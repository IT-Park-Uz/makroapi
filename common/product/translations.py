from modeltranslation.translator import translator, TranslationOptions

from .models import Category, CatalogFile, Product, TopCategory, ProductRegion


class CategoryTranslationOptions(TranslationOptions):
    fields = ['title']


class TopCategoryTranslationOptions(TranslationOptions):
    fields = ['title']


class CatalogFileTranslationOptions(TranslationOptions):
    fields = ['title']


class ProductTranslationOptions(TranslationOptions):
    fields = ['title']


class ProductRegionTranslationOptions(TranslationOptions):
    fields = ['name']


translator.register(Category, CategoryTranslationOptions)
translator.register(TopCategory, TopCategoryTranslationOptions)
translator.register(CatalogFile, CatalogFileTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductRegion, ProductRegionTranslationOptions)
