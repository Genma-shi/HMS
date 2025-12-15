from rest_framework import serializers
from .models import Appointment, VisitHistory

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class VisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitHistory
        fields = '__all__'
