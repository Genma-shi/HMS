# equipment/models.py
from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    last_maintenance = models.DateField(null=True, blank=True)

    def check_availability(self):
        return self.is_available and self.quantity > 0

    def __str__(self):
        return self.name
