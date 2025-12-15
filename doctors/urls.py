from rest_framework import routers
from django.urls import path, include
from doctors.views import DoctorViewSet

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = [
    path('', include(router.urls)),
]
