from django.contrib import admin
from .models import MedicalPrescription


@admin.register(MedicalPrescription)
class MedicalPrescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'disease_name',
        'doctor',
        'issued_at',
        'treatment_duration_days'
    )
    search_fields = ('disease_name',)
