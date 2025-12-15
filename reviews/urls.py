from rest_framework import routers
from django.urls import path, include
from reviews.views import ReviewViewSet

router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]
