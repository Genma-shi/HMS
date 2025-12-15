# strikes/models.py
from django.db import models

class Strike(models.Model):
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='strikes'
    )
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def resolve(self):
        self.is_resolved = True
        self.save()

    def __str__(self):
        return f"Strike for {self.doctor} ({'resolved' if self.is_resolved else 'pending'})"
