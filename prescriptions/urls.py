from rest_framework.routers import DefaultRouter
from .views import MedicalPrescriptionViewSet

router = DefaultRouter()
router.register(
    'prescriptions',
    MedicalPrescriptionViewSet,
    basename='prescriptions'
)

urlpatterns = router.urls
