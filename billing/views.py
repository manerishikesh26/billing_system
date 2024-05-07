from django.shortcuts import render, redirect
from .models import Product, Bill
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'billing/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'billing/add_product.html', {'form': form})

# def generate_bill(request):
#     if request.method == 'POST':
#         form = BillForm(request.POST)
#         if form.is_valid():
#             bill = form.save()
#             return redirect('view_bill', bill_id=bill.id)
#     else:
#         form = BillForm()
#     return render(request, 'billing/generate_bill.html', {'form': form})

def generate_bill(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')
        selected_products = Product.objects.filter(id__in=selected_items)
        total_cost = sum(product.price for product in selected_products)
        context = {
            'selected_products': selected_products,
            'total_cost': total_cost
        }
        return render(request, 'billing/generate_bill.html', context)
    else:
        products = Product.objects.all()
        return render(request, 'billing/select_items.html', {'products': products})

def view_bill(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    return render(request, 'billing/view_bill.html', {'bill': bill})
