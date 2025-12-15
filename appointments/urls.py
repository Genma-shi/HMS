from django.urls import path
from .views import CreateAppointmentAPIView, CancelAppointmentAPIView, DoctorSlotsAPIView

urlpatterns = [
    # Создать запись к врачу
    path('create/', CreateAppointmentAPIView.as_view(), name='create_appointment'),

    # Отменить запись по ID
    path('cancel/<int:pk>/', CancelAppointmentAPIView.as_view(), name='cancel_appointment'),

    # Получить свободные слоты доктора на конкретную дату (YYYY-MM-DD)
    path('doctor-slots/<int:doctor_id>/<str:date>/', DoctorSlotsAPIView.as_view(), name='doctor_slots'),
]
