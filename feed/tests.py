from django.test import TestCase
from .models import Image
from django.contrib.auth.models import User
from users.models import Profile
# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        self.new_profile=Profile.get_profile_by_userid(self.new_user.id)
        self.new_image= Image(image_name='Cycling',image_caption='sahgsbxsahzb',profile=self.new_profile)
        self.new_image.save_image()



    # Tear Down method
    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        Image.objects.all().delete()      

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))    

    # Testing Save Method
    def test_save_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)  

    # Testing get all images Method
    def test_get_all_images_method(self):
        images = Image.get_all_images()
        self.assertTrue(len(images) > 0) 


    # Testing get all images Method
    def test_get_image_by_id_method(self):
        image = Image.get_image_by_id(self.new_image.id)
        self.assertEqual(image.id,self.new_image.id)          


    # Testing delete method
    def test_delete_image(self):
        Image.delete_image(self.new_image.id)
        images = Image.get_all_images()
        self.assertTrue(len(images) == 0)


    # Testing search image by category method
    def test_search_image(self):
        images=Image.search_image('Cyc')
        imagess=Image.search_image('Taa')
        self.assertFalse(len(imagess) > 0)  
        self.assertTrue(len(images) > 0)  


    # Testing filter by userid method
    def test_filter_by_userid(self):
        images=Image.filter_by_userid(self.new_user.id)
        self.assertTrue(len(images) > 0)


       
