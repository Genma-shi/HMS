from rest_framework import viewsets, permissions
from .models import Doctor
from patients.models import Patient
from appointments.models import Appointment
from prescriptions.models import Prescription
from reviews.models import Review
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, PrescriptionSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def patients(self, request):
        doctor = request.user.doctor
        patients = doctor.get_patients()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def appointments(self, request):
        doctor = request.user.doctor
        serializer = AppointmentSerializer(doctor.get_appointments(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_prescription(self, request, pk=None):
        doctor = request.user.doctor
        patient_id = request.data.get('patient')
        description = request.data.get('description')
        patient = Patient.objects.get(id=patient_id)
        prescription = doctor.add_prescription(patient, description)
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def reviews(self, request):
        doctor = request.user.doctor
        serializer = ReviewSerializer(doctor.get_reviews(), many=True)
        return Response(serializer.data)
