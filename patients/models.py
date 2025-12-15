from django.db import models
from accounts.models import User


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_state = models.TextField()
    priority = models.PositiveSmallIntegerField(default=0)
    priority_reason = models.TextField(blank=True)