# Step 4: Define Models for Categories, Products, Orders, and Users
# ------------------------------------------------------------------
# affiliate_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
     
class Order(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   order_date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"Order #{self.id} by {self.user.username}"