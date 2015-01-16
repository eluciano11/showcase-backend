from django.db import models

from autoslug import AutoSlugField

from ..users.models import User
from ..universities.models import University
from ..departments.models import Department


class Project(models.Model):
    class Meta:
        ordering = ['created_at']

    created_by = models.ForeignKey(User)
    university = models.ForeignKey(University)
    department = models.ForeignKey(Department)

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title')
    summary = models.CharField(max_length=140)
    story = models.TextField()
    screenshot = models.FileField(upload_to='screenshot/%Y/%m/%d')

    def __str__(self):
        return self.title
