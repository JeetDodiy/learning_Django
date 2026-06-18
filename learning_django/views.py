from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "first.html")

def home(request):
    djtext = request.GET.get('text','fu')
    djremovepunc = request.GET.get('removepunc','0ff')
    uparcase = request.GET.get('fullcap','off')
    newLineremove = request.GET.get('newlineremove' , 'off')
    spaceRemover = request.GET.get('spaceRemover','off')
    cherCounter = request.GET.get('cherCounter','off')

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
    elif spaceRemover == 'on':
        analyzed = ''
        for index , char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        param = {'purpose': 'Remove space', 'analyze_text': analyzed}
        return render(request, "analyze.html", param)
    elif cherCounter == 'on':
         analyzed = ('No. of characters given in the text are : ' + str(len(djtext)))
         param = {'purpose': 'Count number of characters', 'analyze_text': analyzed}
         return render(request, "analyze.html", param)

    else:
        return HttpResponse("Error")


# def analyze(request):
#     return render(request, "analyze.html")


