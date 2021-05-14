from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')

def result(request):
    text=request.POST.get('text','off')
    punc=request.POST.get('punc','off')
    newline=request.POST.get('newline','off')
    comma=request.POST.get('comma','off')
    punctuations = '''!()-[]{;:'"\,<>}./?@#$%^&*_~'''
    if punc=='on':
        newtext=''
        for i in text:
            if i not in punctuations:
                newtext+=i
        text=newtext
    if newline=='on':
        newtext=''
        for i in text:
            if i!='\n' and i!='\r':
                newtext+=i
        text=newtext
    if comma=='on':
        newtext=''
        for i in range(0,len(text)):
            if (text[i]=='\n' or text[i]=='\r') and (text[i-1]=='\n' or text[i-1]=='\r'):
                newtext+=','
            elif text[i]!='\n' and text[i]!='\r' :
                newtext+=text[i]
        text=newtext
    para={'value':text}               


    return render(request,'result.html',para)

