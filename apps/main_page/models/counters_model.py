from django.core.exceptions import ValidationError
from django.db import models


class Counter(models.Model):
    number = models.PositiveIntegerField(verbose_name='Число блока счетчика')
    icon = models.ImageField(upload_to='images/',
                                       verbose_name='Иконка блока счетчика')
    title = models.CharField(max_length=30,
                                       verbose_name='Заголовок блока счетчика')

    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчик"

    def __str__(self):
        return 'Счетчик обратившихся, выписанных, оперированных и рожденных'