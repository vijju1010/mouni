from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import student
def default(request):
   return HttpResponse("home page")
def subjects(request):
   template = loader.get_template('subjects.html')
   return HttpResponse(template.render())

# Create your views here.
def view1(request):
    return HttpResponse("Hello world!"+request.get_host())


def view2(request):
  mymembers=student.objects.all().values()
  template = loader.get_template('studenthtml.html')
  context={
     'mymembers' : mymembers,
  }

  return HttpResponse(template.render(context,request))


def view3(request):
  #mymembers = Member.objects.all().values()
  template = loader.get_template('html2.html')
  context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
  return HttpResponse(template.render(context, request))
