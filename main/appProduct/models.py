from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = '_categories'
    name = models.CharField(max_length=255)


class Product(models.Model):
    class Meta:
        db_table = '_products'
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name