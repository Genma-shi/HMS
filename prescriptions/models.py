from django.db import models
from django.core.exceptions import ValidationError

from appointments.models import VisitHistory
from doctors.models import DoctorProfile


class MedicalPrescription(models.Model):
    """
    Назначение врача.
    Может создавать ТОЛЬКО терапевт.
    """

    visit = models.OneToOneField(
        VisitHistory,
        on_delete=models.CASCADE,
        related_name='prescription'
    )

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.PROTECT,
        related_name='prescriptions'
    )

    disease_name = models.CharField(
        max_length=255,
        verbose_name='Название болезни'
    )

    medications = models.JSONField(
        verbose_name='Лекарства',
        help_text='[{name, dose, usage}]'
    )

    issued_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата выписки'
    )

    treatment_duration_days = models.PositiveIntegerField(
        verbose_name='Срок лечения (дни)'
    )

    system_recommendations = models.JSONField(
        default=list,
        verbose_name='Рекомендации системы',
        help_text="['Постельный режим', 'Пить больше воды']"
    )

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'

    def clean(self):
        if not self.doctor.is_therapist:
            raise ValidationError(
                'Назначения может делать только врач-терапевт'
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.disease_name} — {self.visit.appointment.patient.user.get_full_name()}"
