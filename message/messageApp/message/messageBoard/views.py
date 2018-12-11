from django.shortcuts import render

from django.views.generic import ListView
from .models import Posts
# Create your views here.

class HomePageView(ListView):
    model=Posts
    context_object_name ='all_post_list'
    template_name='home.html'