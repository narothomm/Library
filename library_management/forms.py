from django import forms 
from .models import Profile

class ProfileForm(forms.ModelForm):#forms.ModelForm:ProfileForm হলো একটি মডেল ফর্ম,যা সরাসরি Django মডেল থেকে ফিল্ডগুলো নেয়।

     class Meta:  #model: কোন মডেলের ভিত্তিতে ফর্মটি তৈরি হবে, সেটি নির্ধারণ করা হয়। এখানে Profile মডেলটি ব্যবহৃত।
        model=Profile
        fields=['bio','website','birthDate']
        
        widgets={
            'birthDate':forms.DateInput(attrs={'type':'date'})
        }
        
 # widgets: নির্দিষ্ট ফিল্ডের জন্য কাস্টম উইজেট বা HTML অ্যাট্রিবিউট সেট করা হয়। এখানে birthDate ফিল্ডে DateInput উইজেট 
 # দেওয়া হয়েছে, যা HTML5 এর তারিখ ইনপুট সমর্থন করে।