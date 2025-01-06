from ..services import ImageService
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Block(models.Model):
    title = models.CharField(max_length=255, verbose_name="Зогловок")
    photo_url = models.ImageField(upload_to='images/', verbose_name="Фото")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageService.convert_to_webp(self, 'photo_url')

    class Meta:
        verbose_name = "Лечебная работа блок"
        verbose_name_plural = "Лечебная работа блоки"

    def __str__(self):
        return self.title


class Department(models.Model):
    ADDRESS_LIST = [
        ('Тоголок Молдо, 1', 'Тоголок Молдо, 1'),
        ('ул. Ахунбаева, 190', 'ул. Ахунбаева, 190'),
        ('Тоголок Молдо, 1 | ул. Ахунбаева, 190', 'Тоголок Молдо, 1 | ул. Ахунбаева, 190')
    ]
    
    name = models.CharField(max_length=255, verbose_name='Название отделения')
    description = CKEditor5Field(verbose_name='Описание отделения')
    photo_url = models.ImageField(upload_to='images/', verbose_name="Фото")
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Блок', related_name='departments')
    address = models.CharField(choices=ADDRESS_LIST, max_length=255, verbose_name='Адрес')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageService.convert_to_webp(self, 'photo_url')

    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделение"

    def __str__(self):
        return self.name
