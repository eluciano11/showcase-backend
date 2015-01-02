from django.db import models


class DepartmentName(models.Model):
    name = models.CharField(max_length='100')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.ForeignKey('DepartmentName')
    university = models.ForeignKey('universities.University')

    def __str__(self):
        return self.name
