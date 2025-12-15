from django.db import models
from patients.models import PatientProfile


class Strike(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    reason = models.TextField()