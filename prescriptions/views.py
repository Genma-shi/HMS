from rest_framework import viewsets
from .models import MedicalPrescription
from .serializers import MedicalPrescriptionSerializer

class MedicalPrescriptionViewSet(viewsets.ModelViewSet):
    queryset = MedicalPrescription.objects.all()
    serializer_class = MedicalPrescriptionSerializer
