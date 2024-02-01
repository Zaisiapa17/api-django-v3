from django.db import models
from appProduct.models import Product
from appCustomer._test_table import table_model

# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = '_customers'
    customer_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

class OrderContainer(models.Model):
    class Meta:
        db_table = '_order_containers'
        unique_together = ('customer', 'product')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"OrderContainer {self.id} - Customer: {self.customer.customer_name}"