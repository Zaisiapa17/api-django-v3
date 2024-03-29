from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ['id', 'product_name', 'price', 'quantity']
