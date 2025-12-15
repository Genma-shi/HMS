from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Администратор'
    DOCTOR = 'DOCTOR', 'Врач'
    PATIENT = 'PATIENT', 'Пациент'


class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices
    )

    is_banned = models.BooleanField(default=False)
    strikes_count = models.PositiveSmallIntegerField(default=0)
