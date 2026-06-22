from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request ,"first1.html")

def about_us_url(request):
    return render(request ,"about_us.html")

def about_url(request):
    return render(request ,"about.html")