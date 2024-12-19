from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from members.models import Member
from members.forms import MemberSearchForm,AddMemberForm,UpdateMemberForm
from.models import Fruits

# Create your views here.
def members_home(request):
   return HttpResponse("members home page")

def members_home(request):
   data= "Members home page"
   return render(request,"home.html",context={"pagetitle":data})

def members_home(request):
  context={
     "pagetitle": "pagetitle well to members home page",
     "content": "content Wellcome everyone thank you for joining our tennis club",
     "footer": "footer 2024 your name" 
     }
  return render(request,"home.html",context)

def add_member(request):
   member=Member(firstname="rai",lastname="roy",age="04")
   member.save()
   return HttpResponse("data add successfully")


def add_multiple_member(request):
   member1=Member(firstname="santo",lastname="hmolla",age="30")
   member2=Member(firstname="sjanifa",lastname="khanom",age="17")
   member3=Member(firstname="johana",lastname="begum",age="18")
   members_list=[member1,member2,member3,]
   
   for x in members_list:
      x.save()
   return HttpResponse("data inserted multiple successfully")


def view_members(request):
   member=Member.objects.all().values()
   context={
      "allMembers":member
   }
   return render(request,'view_members.html',context)


def member_details(request,id): 
   member=Member.objects.get(id=id)
   context={
      "member_details":member
   }
   return render(request,"member_details.html",context)
   


def add_member(request): 
     
      # firstname=request.POST.get("firstname")
      # lastname=request.POST.get("lastname")
      # age=request.POST.get("age")
      # if all([firstname,lastname,age]):
      #    member= Member(firstname=firstname,lastname=lastname,age=age)
       if request.method=="POST":
          form=AddMemberForm(request.POST)
          if form.is_valid():
           form.save()
           #return HttpResponse("New member added successfully")
           return redirect("view_members")
       else:
           form=AddMemberForm()
           context={'form':form}
           return render(request,"add_member.html",context)
   

def search_member(request):
   django_form=MemberSearchForm(request.GET or None)     
   searched_member=[]                                   
   if django_form.is_valid():         #ধরা যাক, একটি Django form-এ ইউজার একটি ফিল্ডে (যেমন query) "Hello" লিখে সাবমিট করেছেন।            
     #query=request.GET.get('query')  # ফর্মটি ভ্যালিড হলে cleaned_data এমন কিছু দেখাবে:{'query': 'Hello'}
     query_value=django_form.cleaned_data.get('query')    #.get('query') ব্যবহার করলে,'query' key-এর মান (value)"Hello" পাওয়া যাবে।            
     searched_member= Member.objects.filter(firstname=query_value) 
     #এই লাইনে Member নামক মডেলের ডাটাবেস থেকে firstname ফিল্ডে query-এর মানের সাথে মিলে যাওয়া রেকর্ডগুলো ফিল্টার করে আনা হচ্ছে।
     #print(django_form )
     #print(searched_member )
   context={
       "members":searched_member,
       "form": django_form                              
    }
   return render(request,'search_member.html',context)


def deleteMember(request,id):
   member=Member.objects.get(id=id)
   member.delete()
   return redirect('view_members')


def updateMember(request,id):
    member=Member.objects.get(id=id)   #ডাটাবেস থেকে নির্দিষ্ট Member অবজেক্ট আনা,এটি Member মডেলের instance
    
    if request.method == "POST":
        memberForm=UpdateMemberForm(request.POST,instance=member)  # ফর্মের ডেটা এবং Member অবজেক্ট ফর্মের সাথে যুক্ত করা
        #memberForm এটি একটি ভ্যারিয়েবল, যা UpdateMemberForm এর একটি ইনস্ট্যান্স ধরে রাখছে।
        if memberForm.is_valid():
            memberForm.save()
            return redirect('view_members')
            print(member)
        else:
            HttpResponse('all data are not valid')
    #GET রিকোয়েস্টে বিদ্যমান Member অবজেক্ট থেকে ফর্ম তৈরি       
    memberForm=UpdateMemberForm(instance=member)
    context={
        "form":memberForm
    }
    return render(request,'update_member.html',context)
 
 
def fruitsData(request):
   mangos=Fruits.objects.all()
   return render(request,'fruitsData.html',{"mango":mangos})
   


def testing(request):
   fruits=['apple','banana','cherry']
   person=[
   {
   "model":"members.json",
   "id": 1,
   "name": "Alice",
   "isStudent": true,
   "courses": ["Math", "Science"],
   "profile": null
   },

   {
      "model":"members.json",
   "id": 2,
   "name": "Blice",
   "isStudent": false,
   "courses": ["Math", "Science"],
   "profile": null

   }
         
   ]
   return JsonResponse({'fruits':fruits})



