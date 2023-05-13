from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

from app.forms import *


def fbv(request):
    return HttpResponse('this request is handled by fbv ')


class CBV(View):
    def get(self,request):
        return HttpResponse('this request is handled by CBV ')
    

def fbv_html(request):
    return render(request,'fbv_html.html')


class CBV_html(View):
    def get(self,request):
        return render (request,'CBV_html.html')
    

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=="POST":
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic inserted successfully')


    return render(request,'fbv_form.html',d)


class CBV_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_form.html',d)

    
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data inserted succesfully')