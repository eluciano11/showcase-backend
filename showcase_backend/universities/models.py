from django.db import models


class University(models.Model):
    class Meta:
        ordering = ['name', 'town']
        verbose_name_plural = 'universities'

    name = models.CharField(max_length=50)
    emblem = models.FileField(upload_to='emblems/%Y/%m/%d')
    town = models.CharField(max_length=30)

    def __str__(self):
        return self.name
