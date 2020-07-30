# I have created this file-- Bhupii

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #param={'Name':'Bhupendra','City':'Burhanpur'}

    return render(request,'index.html');

def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("removepunc ");

def capfirst(request):
    return HttpResponse("captilize first ");

def newlineremove(request):
    return HttpResponse("newline remove  ");

def spaceremove(request):
    return HttpResponse("space remove  ")

def charcount(request):
    return HttpResponse("char count   ");

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default');
    #Taking value of checbox
    removepunc=request.GET.get('removepunc','off');
    uppercase=request.GET.get('uppercase','off');
    charcount=request.GET.get('charcount','off');
    wordcount=request.GET.get('wordcount','off');

#Checking value of checkbox and what method need to be applied.
    param3={};
    param={};
    param1={};
    Flag='';#checking what its following method.
    if removepunc=='on':
        punctuations = '''!@#$%^&*()_+''';
        analyze_data = '';
        for char in djtext:

            if char not in punctuations:
                analyze_data=analyze_data+char;

                param={'purpose':'remove punctuations ','analyzed_Data':analyze_data};
        return render(request,'analyze.html',param);
    elif uppercase== 'on':



        analyze_data= '';

        for char in djtext:
            analyze_data=analyze_data+char.upper();
            print("analyze_data")
            param1 = {'purpose1': 'Uppercase ', 'analyzed_Data1': analyze_data};
            #param1.update(param);
            print(param1)
        return render(request,'analyze.html',param1);
    elif charcount=='on':
        count=0;
        for char in djtext:
            if char!=' ':

                count=count+1;
                print("hi in charcount")
                param={'purpose': 'Uppercase ', 'analyzed_Data': count};

        return render(request, 'analyze.html', param);
    elif wordcount=='on':
        wordlist=djtext.split();
        count=0;
        for char in wordlist:
            count+=1;
            param={'purpose': 'Uppercase ', 'analyzed_Data': count};
        return render(request, 'analyze.html', param);


    else:
        return HttpResponse('Error');





def ex1(request):
    return HttpResponse('''<a href= "https://www.google.com/">GOOGLE</a>''')
