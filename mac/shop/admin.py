from django.contrib import admin
from .models import Product,Tickets,Order,Update
# Register your models here.
admin.site.register(Product)
admin.site.register(Tickets)
admin.site.register(Order)
admin.site.register(Update)