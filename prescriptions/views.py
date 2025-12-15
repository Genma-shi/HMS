from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import MedicalPrescription
from .serializers import MedicalPrescriptionSerializer
from .permissions import IsTherapist


class MedicalPrescriptionViewSet(ModelViewSet):
    """
    CRUD назначений.
    Создание — только терапевт.
    """

    queryset = MedicalPrescription.objects.select_related(
        'visit',
        'doctor',
        'visit__appointment__patient__user'
    )

    serializer_class = MedicalPrescriptionSerializer
    permission_classes = [IsAuthenticated, IsTherapist]
