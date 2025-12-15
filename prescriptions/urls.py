from rest_framework import routers
from django.urls import path, include
from prescriptions.views import PrescriptionViewSet

router = routers.DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet, basename='prescriptions')

urlpatterns = [
    path('', include(router.urls)),
]
