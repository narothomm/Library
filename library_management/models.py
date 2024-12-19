from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    bio=models.TextField()
    website=models.URLField(null=True,blank=True)
    birthDate=models.DateField(null=True,blank=True)
    author=models.OneToOneField(Author,on_delete=models.CASCADE,related_name="profile")
    
    # Profile থেকে Author মডেলে সম্পর্ক স্থাপন করছে। Author মুছে গেলে, সংশ্লিষ্ট Profile-ও মুছে যাবে।on_delete=models.CASCADE
    
    def __str__(self) -> str:
        return "profile of an author"
    
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    published_date=models.DateField(unique=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    #authors=models.ManyToManyField(Author,related_name="books") #many to many relation than get a new table 

 

 ## 2. author=newAuthor কী করে কাজ করে:
#যখন Profile.objects.create(...) কল করা হয়, তখন author=newAuthor যুক্ত করে Profile মডেলের author ফিল্ডে Author 
#মডেলের একটি নির্দিষ্ট instance (newAuthor) সেট করা হয়। Django এই author ফিল্ডকে Author মডেলের Primary Key দিয়ে সংযুক্ত করে।

 #3. ডাটাবেসে সংরক্ষণের প্রক্রিয়া:
#Django OneToOneField বা ForeignKey ব্যবহার করলে, ডাটাবেসে Profile মডেলে একটি author_id নামে কলাম তৈরি হয়।
 #newAuthor এর Primary Key (PK) এই author_id তে সংরক্ষণ করা হয়।
 
#4. on_delete=models.CASCADE কাজ করে কিভাবে:
#on_delete=models.CASCADE নির্দেশ করে, যদি কোনো Author instance ডিলিট করা হয়, তাহলে সেই author এর সাথে সম্পর্কিত
# Profile instance-ও ডিলিট হয়ে যাবে।

#সারসংক্ষেপ:author=newAuthor এর মাধ্যমে Profile মডেলের author ফিল্ডে newAuthor instance যুক্ত হয়। 
#Django ORM এটি ব্যাকগ্রাউন্ডে author_id নামে একটি ফিল্ড তৈরি করে
#যেখানে newAuthor এর Primary Key (যেমন, ID) সংরক্ষণ করা হয়। এর ফলে Profile এবং Author মডেলের মধ্যে একটি সম্পর্ক তৈরি হয়। 




