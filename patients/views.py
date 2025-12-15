from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from appointments.models import VisitHistory


class MyHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        visits = VisitHistory.objects.filter(
            appointment__patient=request.user.patient_profile
        )

        return Response([
            {
                'date': v.created_at,
                'symptoms': v.symptoms
            } for v in visits
        ])
