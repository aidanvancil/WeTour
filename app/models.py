from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=10, null=True)
    personality_traits = models.JSONField(default=list)
    languages = models.JSONField(default=list)
    biography = models.CharField(max_length=200, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class TourGuide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    pay_rate = models.DecimalField(max_digits=8, decimal_places=2)

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    destination = models.CharField(max_length=100)
    num_days = models.IntegerField()
    is_paid = models.BooleanField(null=True)
    description = models.TextField()
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True)