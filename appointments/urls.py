from rest_framework import routers
from django.urls import path, include
from appointments.views import AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls)),
]
