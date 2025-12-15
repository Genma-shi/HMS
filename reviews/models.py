from django.db import models
from accounts.models import User


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given')
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    is_positive = models.BooleanField()