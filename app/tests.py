from django.test import TestCase
from .models import Post, Profile, Comment
# Create your tests here.


class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.picture= Post(name = 'picture1', caption ='water', date ='2021-11-22',user = 'admin',image = 'dsfsd.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.picture,Post))

    def test_save_method(self):
        self.picture.save_image() 
        images = Post.objects.all()  
        self.assertTrue(len(images) > 0) 

    def test_delete_image(self):
        self.picture.save_image()
        self.picture= Post(name = 'picture1', caption ='water', date ='2021-11-22',user = 'admin',image = 'dsfsd.jpg')
        self.picture.save_image()
        self.picture.delete_image()
        deleted = Image.objects.all()
        self.assertEqual(len(deleted),1)