from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import DoctorProfile
from .serializers import DoctorSerializer


class DoctorListAPIView(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailAPIView(RetrieveAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer
