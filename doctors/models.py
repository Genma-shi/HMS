from django.db import models
from accounts.models import User


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_years = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    education = models.JSONField()
    about = models.TextField()
    is_therapist = models.BooleanField(default=False)