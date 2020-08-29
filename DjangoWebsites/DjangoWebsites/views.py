from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("About")


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    nextlineremover=request.POST.get('nextlineremover','off')
    extrasprem=request.POST.get('extrasprem','off')
    if removepunc=='on':
    # analyzed=djtext
        punctuations ='''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Capitalize text','analyzed_text':analyzed}
        djtext=analyzed

    if(nextlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'Next Line Remover','analyzed_text':analyzed}
        djtext=analyzed

    if(extrasprem=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext=analyzed
        
    if(removepunc!="on" and fullcaps!="on" and nextlineremover!="on" and extrasprem!="on" and charcount!="on"):
        return HttpResponse("Please opt any option and try again...")
        
    return render(request,'analyze.html',params)

