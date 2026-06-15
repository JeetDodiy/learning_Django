from django.http import HttpResponse
from django.shortcuts import render
from numpy import char


def index(request):
    return render(request, "first.html")

def home(request):
    djtext = request.GET.get('text','fu')
    djremovepunc = request.GET.get('removepunc','0ff')
    print(djtext)
    print(djremovepunc)
    punctuation = '''!()-[]{};:'",<>. /?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuation:
            analyzed = analyzed + char
    param = {'purpose':'this is that', 'analyze_text': analyzed}
    return render(request, "analyze.html",param)

# def analyze(request):
#     return render(request, "analyze.html")


