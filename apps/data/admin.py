from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models.news_model import New
from .services import TranslatorMediaMixin


class NewAdmin(TranslatorMediaMixin, TranslationAdmin):
    pass


admin.site.register(New, NewAdmin)
