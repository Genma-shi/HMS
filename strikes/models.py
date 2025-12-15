from django.db import models
from accounts.models import DoctorProfile  # <-- импорт из accounts

class Strike(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_strikes')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
