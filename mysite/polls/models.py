from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    
    def __str__(self):
        return self.username
    
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254,
                            unique=True,
                            blank=False)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,
                               on_delete=models.SET_NULL,
                               null=True)
    complete=models.BooleanField(default=False)
    
    def __str__(self):
        return self.customer.name
    @property
    def get_all_sum(self):
        items=self.orderitem_set.all()
        total=sum([item.get_total for item in items])
        return total
    @property
    def get_all_sum(self):
        items=self.orderitem_set.all()
        total=sum([item.quantity for item in items])
        return total
class OrderItem(models.Model):
    order=models.ForeignKey(Order,
                            on_delete=models.SET_NULL,
                            null=True)
    product=models.ForeignKey(Product,
                              on_delete=models.SET_NULL,
                              null=True)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.order.customer.name
    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total
    