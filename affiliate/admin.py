# Step 6: Register Models in Admin Panel
# ---------------------------------------
# affiliate_app/admin.py
from django.contrib import admin
from .models import Category, Product, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
