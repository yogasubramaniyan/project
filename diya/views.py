from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from diya.models import aboutus

# Create your views here.
def home(request):
  context1={
   'aboutus':aboutus.objects.all()
  }
  return render(request, 'diya.html', context1)