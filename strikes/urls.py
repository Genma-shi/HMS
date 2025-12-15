from rest_framework import routers
from django.urls import path, include
from strikes.views import StrikeViewSet

router = routers.DefaultRouter()
router.register(r'strikes', StrikeViewSet, basename='strikes')

urlpatterns = [
    path('', include(router.urls)),
]
