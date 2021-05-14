from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.name

class Tickets(models.Model):
    ticket_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    ticket=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    cartjson=models.CharField(max_length=500)

    def __str__(self):
        return str(self.order_id)

class Update(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.CharField(max_length=50)
    order_update=models.CharField(max_length=500)
    timestamp=models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)+" "+self.order_update[:25]+'...'
        