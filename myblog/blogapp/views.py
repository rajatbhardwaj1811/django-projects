from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    return render(request,'blogapp/home.html',{'posts':Post.objects.all()})

def blogpost(request,id):
    return render(request,'blogapp/blogpost.html',{'post':Post.objects.filter(post_id=id)})