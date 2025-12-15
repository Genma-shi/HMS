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

# Создание профилей для докторов и пациентов
class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100, blank=True)

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    medical_history = models.TextField(blank=True)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'doctor':
            DoctorProfile.objects.create(user=instance)
        elif instance.role == 'patient':
            PatientProfile.objects.create(user=instance)
