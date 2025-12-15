# appointments/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

class Appointment(models.Model):
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    patient = models.ForeignKey(
        'patients.PatientProfile',
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date_time = models.DateTimeField()
    notes = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)

    def confirm(self):
        self.is_confirmed = True
        self.save()

    def cancel(self):
        self.is_confirmed = False
        self.save()

    def is_past(self):
        return self.date_time < timezone.now()

    def __str__(self):
        return f"{self.patient} -> {self.doctor} on {self.date_time}"
