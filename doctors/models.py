# doctors/models.py
from django.db import models
from django.conf import settings

class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialization = models.CharField(max_length=100, blank=True)

    def get_full_name(self):
        return self.user.full_name or self.user.get_full_name()

    def is_available(self):
        # Заглушка, можно добавить реальную логику
        return True

    def __str__(self):
        return f"Dr. {self.get_full_name()} ({self.specialization})"
