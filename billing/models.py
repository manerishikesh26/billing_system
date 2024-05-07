from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()  # New field for description

    def __str__(self):
        return self.name

class Bill(models.Model):
    customer_name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='BillItem')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bill #{self.id} for {self.customer_name}'
        
class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
