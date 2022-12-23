"""from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Nike!")"""
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import nikeApp

def index(request):
  #template = loader.get_template('mynike.html')
  #return HttpResponse(template.render())
  nikeAppMembers = nikeApp.objects.all().values()
  template = loader.get_template('index.html')
  context = {
      'nikeAppMembers': nikeAppMembers,
  }
  return HttpResponse(template.render(context, request))
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['job']
  newmember = nikeApp(firstname=x, lastname=y, jobtitle=z)
  newmember.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  newmember = nikeApp.objects.get(id=id)
  newmember.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = nikeApp.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  job = request.POST['job']
  member = nikeApp.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.jobtitle = job
  member.save()
  return HttpResponseRedirect(reverse('index'))