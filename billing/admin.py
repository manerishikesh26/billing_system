from django.contrib import admin
from .models import Product, Bill, BillItem

admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(BillItem)