from ..services import ImageService, FileValidationService
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class AboutNCOMID(models.Model):
    class Meta:
        verbose_name = 'Все об НЦОМиД'
        verbose_name_plural = 'Все об НЦОМиД'


class History(models.Model):
    description = CKEditor5Field(verbose_name='Текст')
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='history')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'


class AboutUs(models.Model):
    description = CKEditor5Field(verbose_name='Текст')
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='about_us')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Charter(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    files = models.FileField(upload_to='uploads/', verbose_name='Файлы')
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='charter')

    def clean(self):
        super().clean()
        if self.files:
            FileValidationService.validate_pdf(self.files)

    class Meta:
        verbose_name = 'Устав'
        verbose_name_plural = 'Устав'


class Directorate(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = CKEditor5Field(verbose_name='Текст')
    photo = models.ImageField(upload_to='images/', verbose_name="Фото")
    about_ncomid = models.ForeignKey('AboutNCOMID', on_delete=models.CASCADE, related_name='directorate')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageService.convert_to_webp(self, 'photo')

    class Meta:
        verbose_name = 'Дирекция'
        verbose_name_plural = 'Дирекция'