from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Импорт только реально существующих viewset’ов
from doctors.views import DoctorViewSet
from patients.views import PatientViewSet
from prescriptions.views import MedicalPrescriptionViewSet
# Остальные приложения пока не подключаем

# Регистрация роутера
router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'prescriptions', MedicalPrescriptionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API через роутер
    path('api/', include(router.urls)),

    # DRF Spectacular (OpenAPI / Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
