from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'date_of_birth', 'medical_history']
