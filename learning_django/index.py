from django.shortcuts import render

def index(request):
    return render(request ,"first1.html")

def about_us_url(request):
    return render(request ,"about_us.html")

def about_url(request):
    return render(request ,"about.html")
def error_404(request):
    return  render(request,"eror_404.html")