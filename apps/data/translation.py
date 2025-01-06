from modeltranslation.translator import translator, TranslationOptions
from .models.news_model import New


class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(New, NewTranslationOptions)