from rest_framework import serializers
from .models import Doctor
from accounts.models import CustomUser

class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'specialization']
