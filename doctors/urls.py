from django.urls import path
from .views import DoctorListAPIView, DoctorDetailAPIView

urlpatterns = [
    path('', DoctorListAPIView.as_view()),
    path('<int:pk>/', DoctorDetailAPIView.as_view()),
]
