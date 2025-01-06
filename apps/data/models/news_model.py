from django.db import models
from ..services import ImageService


class New(models.Model):
    title = models.CharField(verbose_name='Заголовок новости',
                             max_length=100)
    text = models.TextField(verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    img = models.ImageField(upload_to='images/',
                            verbose_name='Картинка новости')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ImageService.convert_to_webp(self, 'img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
