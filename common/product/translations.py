from modeltranslation.translator import translator, TranslationOptions

from .models import Category, CatalogFile, Product


class CategoryTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(Category, CategoryTranslationOptions)


class CatalogFileTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(CatalogFile, CatalogFileTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(Product, ProductTranslationOptions)
