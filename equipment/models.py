from django.db import models


class Equipment(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    is_working = models.BooleanField(default=True)