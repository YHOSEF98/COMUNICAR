import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reques):
    return render(reques, "appcomunicar/index.html")

def contacto(reques):
    return render(reques, "appcomunicar/contact.html")

def blog(reques):
    return render(reques, "appcomunicar/blog.html")

def servicios(reques):
    return render(reques, "appcomunicar/technology.html")

def careers(reques):
    return render(reques, "appcomunicar/careers.html")

def single(reques):
    return render(reques, "appcomunicar/single.html")

def about(reques):
    return render(reques, "appcomunicar/about.html")