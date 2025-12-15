from rest_framework import serializers
from .models import Patient
from appointments.models import Appointment
from prescriptions.models import Prescription
from reviews.models import Review
from doctors.models import Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'date_of_birth', 'medical_history']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'datetime', 'status', 'equipment']

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'description', 'date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'doctor', 'rating', 'comment', 'date']
