from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "first.html")

def home(request):
    djtext = request.GET.get('text','fu')
    djremovepunc = request.GET.get('removepunc','0ff')
    uparcase = request.GET.get('fullcap','off')
    newLineremove = request.GET.get('newlineremove' , 'off')

    if djremovepunc == 'on':
        punctuation = '''!()-[]{};:'",<>.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose':'this is that', 'analyze_text': analyzed}
        return render(request, "analyze.html",param)
    elif uparcase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed =  analyzed + char.upper()
        param = {'purpose':'Change to uppercase', 'analyze_text': analyzed}
        return render(request, "analyze.html",param)
    elif newLineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n":

                analyzed = analyzed + char
        param = {'purpose': 'Remove new Line', 'analyze_text': analyzed}
        return render(request, "analyze.html", param)
    else:
        return HttpResponse("Error")

# def analyze(request):
#     return render(request, "analyze.html")


