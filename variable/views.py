from django.shortcuts import render,redirect
#from django.http import HttpResponse,JsonResponse
from members.models import Member
from django.db.models import Q
#from members.forms import MemberSearchForm,AddMemberForm,UpdateMemberForm

# Create your views here.

def variable_home(request):
   #variables=Member.objects.all().values()
   #variables=Member.objects.all().values_list('firstname','lastname','age')
   #variables=Member.objects.filter(lastname='Roy',age=45).values()
   #variables=Member.objects.filter(lastname='Roy',age=45).values() | Member.objects.filter(lastname='ahmed',age=30).values()
   #variables=Member.objects.filter(Q(firstname='narothom') | Q(lastname='ahmed') | Q(age=45)).values() 
   #variables=Member.objects.filter(Q(firstname__startswith='n')).values()  
   variables=Member.objects.all().order_by('firstname').values()   
   #variablelist=list(variables)
   print(variables)          #this is console print line
   
   context={
      "myVariables":variables,
      "greetings1": 1,
      "greetings2": 5
   }
   return render (request,"variable/home.html",context)