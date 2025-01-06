from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class GeneralStructure(models.Model):    
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = CKEditor5Field(verbose_name='Текст контента')
    
    class Meta:
        verbose_name = "Общая структура НЦОМИД"
        verbose_name_plural = "Структура"
    
    def __str__(self):
        return self.title