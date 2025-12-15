from django.db import models
from datetime import timedelta
from django.utils import timezone
from doctors.models import DoctorProfile
from patients.models import PatientProfile


class AppointmentStatus(models.TextChoices):
    SCHEDULED = 'SCHEDULED', 'Запланирован'
    CANCELLED = 'CANCELLED', 'Отменён'
    COMPLETED = 'COMPLETED', 'Завершён'
    NO_SHOW = 'NO_SHOW', 'Не пришёл'


class Appointment(models.Model):
    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.SCHEDULED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self.start_time + timedelta(hours=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.patient.user.get_full_name()} → {self.doctor.user.get_full_name()}'


class VisitHistory(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='visit_history'
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"История визита: {self.appointment}"
