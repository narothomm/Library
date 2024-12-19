from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DocumentForm
from . models import Document

# Create your views here.
from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')  
    else:
        form = DocumentForm()
        documents=Document.objects.all()
        
    context = {
        'form': form,
        'documents':documents
    }
    return render(request, 'fileUpload/file_upload.html', context)
