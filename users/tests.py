from django.test import TestCase
from .models import Profile
import datetime as dt
from django.contrib.auth.models import User
# Create your tests here.


class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user= User(username='denno',email='test@gmail.com',password='moringa#23')
        self.new_user.save()

        self.new_profile=Profile(user=self.new_user)
        self.new_profile.save_profile()


    # Tear Down method
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))    

    # Testing Save Method
    def test_save_method(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)  

    # Testing get all profiles Method
    def test_get_all_profiles_method(self):
        self.new_user1= User(username='dennoi',email='testt@gmail.com',password='moringa#23')
        self.new_user1.save()
        self.new_profile1=Profile(user=self.new_user1)
        self.new_profile1.save_profile()
        profiles = Profile.get_all_profiles()
        self.assertTrue(len(profiles) == 2)


    # Testing get_profile_by_userid Method
    def test_get_profile_by_userid(self):
        profile = Profile.get_profile_by_userid(self.new_user.id)
        self.assertEqual(profile.id,self.new_profile.id)          


    # Testing delete method
    def test_delete_profile(self):
        Profile.delete_profile(self.new_profile.id)
        profiles = Profile.get_all_profiles()
        self.assertTrue(len(profiles) == 0)






