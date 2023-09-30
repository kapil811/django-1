from django.http import HttpResponse
from django.shortcuts import render


''' Welcome To My First Django Site : a sample site using html, css, bootstrap and django.
In this site i had worked with urls, views and templates. i had send data from views to templates using dict[ param= {'data1':output1}] and gained data from templates in views using request.POST.get('element_name')
'''
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
     return render(request,'contactus.html')

def edit(request):
    text = request.POST.get('text', 'default')
    cap =  request.POST.get('capitalize','off')
    punc = request.POST.get('removepunc','off')
    
    output1 =""
    output2 =""


    if( cap == "on"):
                output1 = text.upper()
    else:
         output1 = " switch on the key to get updated text"

    if( punc == "on"):
        puncs = ",.<>/?;:'+_=-@#$%^!`{}[]_~%*&()"
        for char in text:
            if char not in puncs:
                output2 = output2 + char
    else:
         output2 = " switch on the key to get updated text"


    

    params = {'data1' : output1 , 'data2': output2,}
     
    return render(request,'edit.html',params)