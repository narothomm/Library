# Step 7: Views for User Authentication, Product Listing, Detail, and Ordering
# -----------------------------------------------------------------------------
# affiliate_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Order

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'affiliate/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'affiliate/product_detail.html', {'product': product})
 
@login_required
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Order.objects.create(product=product, user=request.user)
    messages.success(request, 'Order placed successfully!')
    return redirect('product_list')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'affiliate/login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')