from django import forms
from.models import Member
#যেখানে শুধু ব্যবহারকারী কিছু সার্চ (search) করবে। এই সার্চের ডাটা ডাটাবেসে সংরক্ষণ করার দরকার নেই। সেক্ষেত্রে, আমরা forms.Form ব্যবহার করব।
#এখানে একটি query নামের ইনপুট ফিল্ড থাকবে। (use Only search)
class MemberSearchForm(forms.Form): 
    query=forms.CharField()
    
#আপনি যখন ডাটাবেসে ডাটা সংরক্ষণ বা আপডেট করতে চান, তখন forms.ModelForm ব্যবহার করবেন। (use Save and update)
#AddMemberForm ফর্মটি সরাসরি Member মডেলের সাথে যুক্ত। মডেলের firstname, lastname, এবং age ফিল্ডগুলো স্বয়ংক্রিয়ভাবে ফর্মে যুক্ত হবে।
class AddMemberForm(forms.ModelForm):
     class Meta:
         model=Member
         fields=["firstname","lastname","age"]
         

class UpdateMemberForm(forms.ModelForm):
     class Meta:
         model=Member
         fields=["firstname","lastname","age"]