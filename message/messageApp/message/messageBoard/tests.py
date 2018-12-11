from django.test import TestCase

from django.test import Client
from .models import Posts
from django.urls import reverse

# Create your tests here.
class HomePageViewTest(TestCase):

    def setUp(self):
        self.client=Client()
        
    def test_home_view_exit_at_location(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_view_url_by_name(self):
        response=self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    
    
class PostModelTest(TestCase):
    def setUp(self):
        self.mytest='just test'
        Posts.objects.create(text=self.mytest)

    def test_text_content(self):
        post=Posts.objects.get(id=1)
        expected_text_contnent= f"{post.text}"
        self.assertEqual(expected_text_contnent,self.mytest)
