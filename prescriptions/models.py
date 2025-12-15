# prescriptions/models.py
from django.db import models

class Prescription(models.Model):
    appointment = models.OneToOneField(
        'appointments.Appointment',
        on_delete=models.CASCADE,
        related_name='prescription'
    )
    medication = models.TextField()
    dosage = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Prescription for {self.appointment.patient}"
