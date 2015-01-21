from django.db import models

from autoslug import AutoSlugField


def populate_university_slug(instance):
    return instance.get_university_fullname()


class University(models.Model):
    class Meta:
        ordering = ['name', 'town']
        verbose_name_plural = 'universities'

    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=populate_university_slug, unique=True)
    emblem = models.FileField(upload_to='emblems/%Y/%m/%d')
    town = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_university_fullname(self):
        return '%s %s' % (self.name, self.town)
