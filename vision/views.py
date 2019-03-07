#from django.shortcuts import render
#from django.utils import timezone
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm
#from django.shortcuts import redirect

# Create your views here.
def base(request):
    return  render(request, 'base.html', {})
