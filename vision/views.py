#from django.shortcuts import render
#from django.utils import timezone
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm
#from django.shortcuts import redirect
import os

# Create your views here.
def linia42(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "vision/static"), ]
    data = {'BASE_DIR':BASE_DIR, 'STATICFILES_DIRS':STATICFILES_DIRS}
    return  render(request, 'linia42.html', context=data)
