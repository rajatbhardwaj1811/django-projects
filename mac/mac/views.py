from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("welcome to home")
    return render(request,'home.html')