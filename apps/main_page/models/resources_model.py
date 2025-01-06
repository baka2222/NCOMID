from django.db import models


class Resource(models.Model):
    class Meta:
        verbose_name = "Ресурсы"
        verbose_name_plural = "Ресурсы"

 
class Journal(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    resource = models.ForeignKey(Resource,
                                 on_delete=models.CASCADE,
                                 related_name='journal')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ресурс журанала"
        verbose_name_plural = "Ресурсы журанала"


class Report(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    resource = models.ForeignKey(Resource,
                                 on_delete=models.CASCADE,
                                 related_name='report')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ресурс отчёта"
        verbose_name_plural = "Ресурсы отчёта"


class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    resource = models.ForeignKey(Resource,
                                 on_delete=models.CASCADE,
                                 related_name='link')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ресурс ссылки"
        verbose_name_plural = "Ресурсы ссылки"
    