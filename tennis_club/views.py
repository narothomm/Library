from django.http import HttpResponse
from django.shortcuts import render

def app_home(request):
   return render(request,'app_home.html')