# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True,
        validators=[RegexValidator(r'^\+?\d{9,15}$', 'Enter a valid phone number')]
    )
    full_name = models.CharField(max_length=150, blank=True)

    def is_doctor(self):
        return self.role == 'doctor'

    def is_patient(self):
        return self.role == 'patient'

    def is_admin(self):
        return self.role == 'admin'

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'doctor':
            from doctors.models import DoctorProfile
            DoctorProfile.objects.create(user=instance)
        elif instance.role == 'patient':
            from patients.models import PatientProfile
            PatientProfile.objects.create(user=instance)
