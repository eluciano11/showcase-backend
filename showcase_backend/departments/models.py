from django.db import models


class DepartmentName(models.Model):
    name = models.CharField(max_length='100')


class Department(models.Model):
    name = models.ForeignKey('DepartmentName')
    university = models.ForeignKey('universities.University')
