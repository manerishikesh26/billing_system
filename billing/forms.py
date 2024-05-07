from django import forms
from .models import Product, Bill

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['customer_name']
