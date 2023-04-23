from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
import requests
import environ


env = environ.Env()
environ.Env.read_env()
img_key = env('IMAGE_API_KEY')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=10, null=True)
    personality_traits = models.JSONField(default=list)
    languages = models.JSONField(default=list)

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
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bio= models.CharField(max_length=200, null=True)
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    destination = models.CharField(max_length=100)
    picture = models.URLField(null=True)

    def generate_map_image(self):
        IMAGE_API_KEY = ''
        LOCATION = self.destination

        # Set the query parameters for the API request
        params = {
            'key': img_key,
            'size': '300,300',
            'center': LOCATION,
            'zoom': 12,
            'format': 'png'
        }

        response = requests.get('http://www.mapquestapi.com/staticmap/v5/map', params=params)
        self.picture = response.url
        self.save()
        