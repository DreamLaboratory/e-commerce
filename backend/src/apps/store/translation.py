from modeltranslation.translator import TranslationOptions, translator

from .models import Product


# for Person model
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Product, ProductTranslationOptions)
