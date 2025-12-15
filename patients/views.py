from rest_framework import viewsets, permissions
from .models import Patient
from appointments.models import Appointment
from prescriptions.models import Prescription
from reviews.models import Review
from .serializers import PatientSerializer, AppointmentSerializer, PrescriptionSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def appointments(self, request):
        patient = request.user.patient
        serializer = AppointmentSerializer(patient.get_appointments(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def prescriptions(self, request):
        patient = request.user.patient
        serializer = PrescriptionSerializer(patient.get_prescriptions(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        patient = request.user.patient
        doctor_id = request.data.get('doctor')
        rating = request.data.get('rating')
        comment = request.data.get('comment')
        doctor = Doctor.objects.get(id=doctor_id)
        review = patient.add_review(doctor, rating, comment)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
