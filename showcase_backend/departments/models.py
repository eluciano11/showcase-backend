from django.db import models

from autoslug import AutoSlugField


class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
