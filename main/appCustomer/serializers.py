from rest_framework import serializers
from . import models


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['id', 'customer_name', 'phone', 'email']


class ItemsCheckOutSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
    product_price = serializers.CharField(source='product.price', read_only=True)

    class Meta:
        model = models.OrderContainer
        fields = ['id', 'product_name', 'product_price', 'created_at', 'updated_at']