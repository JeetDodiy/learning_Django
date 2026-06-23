from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "first.html")


def home(request):
    djtext = request.POST.get('text', 'fu')
    djremovepunc = request.POST.get('removepunc', '0ff')
    uparcase = request.POST.get('fullcap', 'off')
    newLineremove = request.POST.get('newlineremove', 'off')
    spaceRemover = request.POST.get('spaceRemover', 'off')
    cherCounter = request.POST.get('cherCounter', 'off')

    if djremovepunc == 'on':
        punctuation = '''!()-[]{};:'",<>.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose': 'this is that', 'analyze_text': analyzed}
        djtext = analyzed
    if uparcase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Change to uppercase', 'analyze_text': analyzed}
        djtext = analyzed
    if newLineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        param = {'purpose': 'Remove new Line', 'analyze_text': analyzed}
        djtext = analyzed

    if spaceRemover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        param = {'purpose': 'Remove space', 'analyze_text': analyzed}
        djtext = analyzed
    if cherCounter == 'on':
        analyzed = ('No. of characters given in the text are : ' + str(len(djtext)))
        param = {'purpose': 'Count number of characters', 'analyze_text': analyzed}
    if (djremovepunc != 'on' and uparcase != 'on' and newLineremove != 'on' and spaceRemover != 'on'):
        return render(request, "eror_404.html")
    return render(request, "analyze2.html", param)

# def analyze(request):
# return render(request, "analyze21.html")
