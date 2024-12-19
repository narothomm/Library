from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Author,Profile,Book
from .forms import ProfileForm
from django.db.models import Avg,Sum,Count

# # Create your views here.
# def home(request):
#    return render(request,'library_management/home.html')





def testing(request):
    def addProfile():
        try:
            #author=Author.objects.get(id=4)       
            # Create a new Author instance
            newAuthor=Author.objects.create(name="Author six", email="Author5@gmail.com")
            
            # Create a Profile for the newly created author
            profile = Profile.objects.create(
            bio="author sixe bio",
            website="https://authorsix.com",
            birthDate="1990-02-15",
            author=newAuthor  # (প্রথমে তৈরি করা Author-এর সাথে Profile মডেলটি সংযুক্ত)।
            )
            
            # Successful creation response
            return HttpResponse( "Author Profile have been created")
      
        except:
            return HttpResponse("The profile of this author already exists") 
        
    #return addProfile()
    
    def addauthor():
        Author.objects.create(name="author eight",email="authoreight@gmail.com")
        return HttpResponse("author eight created")
    # return addauthor()
    
    def testManyToOneRelation():
        author=Author.objects.get(id=2)
        books=Book.objects.all()
        booklist=[]
        for book in books:
            if book.author_id==author.id:
                book_data={
                    "title":book.title,
                    "published_date":book.published_date,
                    "author_email":book.author.email
                }
                booklist.append(book_data)
        return JsonResponse({"books":booklist})
    #return testManyToOneRelation() 
    
    def testManyToOneRelation():
        author=Author.objects.get(id=2)
        books=author.books.all()
        bookList=[]
        
        for book in books:
            bookList.append(
                {
                    "title":book.title,
                    "published_date":book.published_date
                }
                )
            #print(book.title,book.published_date)
        return JsonResponse({"books":bookList})
    #return testManyToOneRelation()
    

    def testManyToManyRelation():
        author1=Author.objects.get(id=1)
        author2=Author.objects.get(id=2)
        author3=Author.objects.get(id=7)
        author3=Author.objects.get(id=8)
        
        book=Book.objects.get(id=1)
        book.authors.add(author1,author2,author3)
        
        authors=[]
        
        for author in book.authors.all():
             authors.append({
                "name":author.name,
                "email":author.email,
                "bio":author.profile.bio if hasattr (author,'profile') else None,
                "website":author.profile.website if hasattr (author,'profile') else None
             })    
        #authors=[{"name":author.name, "email":author.email} for author in book.authors.all()]   
            
        return JsonResponse({"authors":authors})
    return testManyToManyRelation()  
 
 
def library_status(request):
    # লাইব্রেরির সামগ্রিক স্ট্যাটাস
    library_status = Book.objects.aggregate(
        average_price=Avg('price'),
        total_books=Count('id'),
        total_price=Sum('price')
    )

    # লেখকগণ এবং তাদের বইয়ের তথ্য and add extra field
    authors1 = Author.objects.annotate(
        total_books=Count('books'),
        avg_book_price=Avg('books__price')  #এখানে books হলো Author মডেলের সঙ্গে সম্পর্কিত Book মডেলের related_name 
        # বা ফিল্ড। __price দিয়ে ইঙ্গিত করা হয়েছে যে Book মডেলের price ফিল্ড ব্যবহার করা হবে।
        #প্রতিটি Author-এর অধীন থাকা বইগুলোর price ফিল্ড থেকে গড় (average) গণনা করে, যা avg_book_price নামে 
        #একটি নতুন ফিল্ড হিসেবে যোগ হয়।
    )
    #print(authors1.values())
    authors2=Author.objects.prefetch_related('books')
    books=Book.objects.select_related('author')
    print(books)
    # কন্টেক্সটে তথ্য পাঠানো
    context = {
        "library_status": library_status,  
        "authors1": authors1,
        'authors2': authors2,
        'books':books
    }
    return render(request, 'library_management/library_status.html', context)  
               
       
                
def home(request):
    author=Author.objects.all()
    data={
        "authors":author
    }
    return render(request,'library_management/home.html',data)


def addProfile(request,id):
    #try:
    author=Author.objects.get(id=id)
    if request.method=="POST":
        profileFormData=ProfileForm(request.POST)
        if profileFormData.is_valid():
                profile=profileFormData.save(commit=False)
                profile.author=author
                profile.save()
                return redirect('library_home')
            
    else:
        form = ProfileForm()
        context={
        "form":form
        }
   
    
        return render(request,'library_management/addProfile.html',context)
    #except:
    return HttpResponse("something went wrong") 
 
     
def addBook(request):
    author=Author.objects.get(id=2)
    book=Book.objects.create(title="last'spoem",published_date="2015-01-14", author=author)
    return HttpResponse("Book lastspoem added successfull")    
                   
 
