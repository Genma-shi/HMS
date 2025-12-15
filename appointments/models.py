from django.db import models
from accounts.models import DoctorProfile, PatientProfile

class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    reason = models.TextField(default='Не указано')
