from django.shortcuts import render,redirect
from django.http  import HttpResponse
# Create your views here.


def home_page(request):


  return HttpResponse('Welcome to Instagram')
