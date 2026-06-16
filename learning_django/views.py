from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "first.html")

def home(request):
    djtext = request.GET.get('text','fu')
    djremovepunc = request.GET.get('removepunc','0ff')
    if djremovepunc == 'on':
        punctuation = '''!()-[]{};:'",<>.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose':'this is that', 'analyze_text': analyzed}
        return render(request, "analyze.html",param)
    else:
        return HttpResponse("Error")

# def analyze(request):
#     return render(request, "analyze.html")


