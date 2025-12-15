from datetime import timedelta
from django.utils import timezone
from .models import Appointment

def get_free_slots(doctor, date):
    slots = []
    start = timezone.make_aware(timezone.datetime.combine(date, timezone.datetime.min.time()).replace(hour=9))
    end = timezone.make_aware(timezone.datetime.combine(date, timezone.datetime.min.time()).replace(hour=18))

    while start < end:
        if not Appointment.objects.filter(doctor=doctor, start_time=start).exists():
            slots.append(start)
        start += timedelta(hours=1)

    return slots
