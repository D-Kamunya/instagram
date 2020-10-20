from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from users.models import Profile

class Image(models.Model):
    """
    Image class to define Image Objects
    """
    image_name = models.CharField(max_length =150)
    image_path = ImageField(blank=True, manual_crop="")
    image_caption = models.CharField(max_length =255)
    profile = models.ForeignKey(Profile,
    on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)
    comments=models.IntegerField(default=0)

    def __str__(self):
        return self.image_name 


    class Meta:
        ordering = ['upload_date'] 

    def save_image(self):
      '''
      Saves image instance to db
      '''
      self.save()


    @classmethod
    def get_all_images(cls):
      '''
      Returns all image objects from db
      '''
      images=cls.objects.all()
      return images 


    @classmethod
    def get_image_by_id(cls,id):
      '''
      Returns image based on its id
      '''
      image=cls.objects.get(id=id)
      return image



    @classmethod
    def delete_image(cls,id):
      '''
      Deletes image based on its id
      '''
      cls.objects.filter(id=id).delete()
      

    @classmethod
    def search_image(cls,image_name):
      '''
      Allows us to search for an image using its namw.
      '''
      images=cls.objects.filter(image_name__icontains=image_name)
      return images



    @classmethod
    def filter_by_userid(cls,user_id):
      """
      Allows us to filter images by the user posted.
      """
      images=cls.objects.filter(profile__user_id=user_id)
      return images



class Like(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(Image,on_delete=models.CASCADE)