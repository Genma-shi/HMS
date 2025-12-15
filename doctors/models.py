from django.db import models
from accounts.models import CustomUser

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor')
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.full_name
