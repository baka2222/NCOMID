from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ..services import ImageService, FileValidationService


class ScientificActivity(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Текст блока Научной деятельности')
    img = models.ImageField(upload_to='images/', verbose_name='фото')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageService.convert_to_webp(self, 'img')

    class Meta:
        verbose_name = "Начная деятельность"
        verbose_name_plural = "Научные деятельности"

    def __str__(self):
        return self.title


class ScientificActivityContent(models.Model):
    title_content = models.TextField(verbose_name='Заголовок контента')
    text_content = CKEditor5Field(verbose_name='Текст контента',
                                 null=True,
                                 blank=True)
    block = models.ForeignKey(ScientificActivity,
                              on_delete=models.CASCADE,
                              verbose_name='Блок',
                              related_name='content')

    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контенты"

    def __str__(self):
        if self.title_content:
            return self.title_content
        else:
            pass


class Document(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок Документа')
    scientific_act = models.ForeignKey(ScientificActivityContent, related_name='documents', on_delete=models.CASCADE)
    pdf = models.FileField(verbose_name='PDF Документ', upload_to='documents/')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def clean(self):
        super().clean()
        if self.pdf:
            FileValidationService.validate_pdf(self.pdf)