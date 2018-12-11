from django.test import TestCase

from django.test import Client
from .models import Posts

# Create your tests here.
""" Testing the Home View """

class SimpleTest(TestCase):

    def setUp(self):
        self.client=Client()
        
    def test_home_view(self):
        response=self.client.get('/')

        self.assertEqual(response.status_code,200)
    
  """ Testinf the Posts model"""  
  
class PostModelTest(TestCase):
    def setUp(self):
        self.mytest='just test'
        Posts.objects.create(text=self.mytest)

    def test_text_content(self):
        post=Posts.objects.get(id=1)
        expected_text_contnent= f"{post.text}"
        self.assertEqual(expected_text_contnent,self.mytest)

