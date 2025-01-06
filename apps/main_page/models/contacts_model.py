from django.db import models

class Contacts(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=20)
    text = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='contacts/', verbose_name='Иконка')
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=30)
    url = models.URLField(verbose_name='Ссылка')
    icon = models.ImageField(verbose_name='Иконка', upload_to='social_media/')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.title
        