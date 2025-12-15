from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment
from accounts.models import DoctorProfile
from .services import get_free_slots
from datetime import timedelta, datetime
from django.utils import timezone
from appointments.serializers import AppointmentSerializer
from rest_framework import viewsets

class CreateAppointmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        doctor = DoctorProfile.objects.get(id=request.data['doctor_id'])
        patient = request.user.patient_profile

        start = timezone.make_aware(datetime.fromisoformat(request.data['start_time']))
        end = start + timedelta(hours=1)

        Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            start_time=start,
            end_time=end
        )
        return Response({'message': 'Запись создана'})


class CancelAppointmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment.status = 'CANCELLED'
        appointment.save()
        return Response({'message': 'Запись отменена'})


class DoctorSlotsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, doctor_id, date):
        doctor = DoctorProfile.objects.get(id=doctor_id)
        free_slots = get_free_slots(doctor, timezone.datetime.fromisoformat(date).date())
        return Response({'doctor_id': doctor.id, 'free_slots': free_slots})

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer