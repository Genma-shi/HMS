from django.db import models
from accounts.models import CustomUser

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient')
    date_of_birth = models.DateField(null=True, blank=True)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.full_name
