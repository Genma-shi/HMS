from rest_framework import serializers
from .models import MedicalPrescription

class MedicalPrescriptionSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.full_name', read_only=True)
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = MedicalPrescription
        fields = ['id', 'doctor', 'doctor_name', 'patient', 'patient_name', 'description', 'created_at']
