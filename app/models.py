from django.db import models
from django.contrib.auth.models import User

class User(User):
    phone_number = models.CharField(max_length=20)

class TourGuide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    gender = models.CharField(max_length=10)
    personality_traits = models.JSONField(default=list)
    languages = models.JSONField(default=list)
    pay_rate = models.DecimalField(max_digits=8, decimal_places=2)

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    destination = models.CharField(max_length=100)
    num_days = models.IntegerField()
    description = models.TextField()
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True)