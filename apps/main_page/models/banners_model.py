from django.db import models
from ..services import ImageService, validate_image_min_dimensions

class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    img = models.ImageField(upload_to='banner/', verbose_name='фото', validators=[validate_image_min_dimensions])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageService.convert_to_webp(self, 'img')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'

    def __str__(self):
        return self.title
