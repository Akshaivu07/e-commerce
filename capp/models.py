from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=255,null=True)

    def get_absolute_url(self):
        return reverse('category_page', args=[str(self.pk)])

class Product(models.Model):
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=255,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to="image/",null=True)

class Client(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    u_address=models.CharField(max_length=255,null=True)
    u_contact=models.IntegerField(null=True)
    u_image=models.ImageField(upload_to="image/",null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price



