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
    djtext=request.POST.get('text','default');
    #Taking value of checbox
    removepunc=request.POST.get('removepunc','off');
    uppercase=request.POST.get('uppercase','off');
    newlineremove=request.POST.get('newline','off');
    

#Checking value of checkbox and what method need to be applied.


    if removepunc=='on':
        punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~ ''';
        analyze_data = '';
        for char in djtext:

            if char not in punctuations:
                analyze_data=analyze_data+char;

                param={'purpose':'remove punctuations ','analyzed_Data':analyze_data};
                djtext=analyze_data;
        #return render(request,'analyze.html',param);
    if uppercase== 'on':

        analyze_data= '';

        for char in djtext:
            analyze_data =analyze_data+char.upper();
            # print(analyze_data)
            param = {'purpose': 'Uppercase ', 'analyzed_Data': analyze_data};
            # param1.update(param);
            djtext=analyze_data;
            # print(param1)
        # return render(request, 'analyze.html', param);

    if newlineremove=='on':
        analyze_data='';
        for char in djtext:
            if char not in ["\r","\n"]:
                analyze_data=analyze_data+char;


                param={'purpose':'Newlineremover', 'analyzed_Data': analyze_data};

    return render(request, 'analyze.html', param);









def ex1(request):
    return HttpResponse('''<a href= "https://www.google.com/">GOOGLE</a>''')
def about(request):
    return  HttpResponse("<h1>You are at about Page.    </h1>");
