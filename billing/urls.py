from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('view_bill/<int:bill_id>/', views.view_bill, name='view_bill'),
    path('select_items/', views.generate_bill, name='select_items'),

]
