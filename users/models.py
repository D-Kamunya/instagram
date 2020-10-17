from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt

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
    def get_all_profiles(cls):
      '''
      Returns all profile objects from db
      '''
      profiles=cls.objects.all()
      return profiles 


    @classmethod
    def get_profile_by_userid(cls,userid):
      '''
      Returns profile based on user id
      '''
      profile=cls.objects.filter(user_id=userid)
      return profile


    @classmethod
    def delete_profile(cls,userid):
      '''
      Deletes profile based on user id
      '''
      cls.objects.filter(user_id=userid).delete()    

