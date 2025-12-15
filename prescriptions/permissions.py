from rest_framework.permissions import BasePermission


class IsTherapist(BasePermission):
    """
    Доступ только для врачей-терапевтов
    """

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if not hasattr(user, 'doctor_profile'):
            return False

        return user.doctor_profile.is_therapist
