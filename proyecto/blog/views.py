from django.shortcuts import render
from .models import entry


def home (request):

    author_info ={
        "entry" : entry.objects.all()   
    }

    return render(request, "blog/home.html")

def about (request):
    return render(request, "blog/about.html")