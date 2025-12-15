from django.db import models
from accounts.models import CustomUser

class MedicalPrescription(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='prescriptions_given')
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='prescriptions_received')
    description = models.TextField(default='Не указано')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.id} for {self.patient.full_name}"
