from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = ImageField(blank=True, manual_crop="")
    bio = models.TextField(max_length=500, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
      '''
      Saves profile instance to db
      '''
      self.save()


    @classmethod
    def get_all_profiles(cls,current_user):
      '''
      Returns all profile objects from db
      '''
      profiles=cls.objects.exclude(user=current_user)
      return profiles 


    @classmethod
    def get_profile_by_userid(cls,userid):
      '''
      Returns profile based on user id
      '''
      profile=cls.objects.get(user=userid)
      return profile


    @classmethod
    def delete_profile(cls,userid):
      '''
      Deletes profile based on user id
      '''
      cls.objects.get(user_id=userid).delete()    



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
