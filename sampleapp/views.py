from django.shortcuts import render 
from django.http import HttpResponse

def samplefn(request):
    return HttpResponse('abc')

def firstfn(request):
    return render(request,'firstpage.html')        
