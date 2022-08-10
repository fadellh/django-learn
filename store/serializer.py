from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from decimal import Decimal

from store.models import Collection, Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=225)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    collection = serializers.StringRelatedField()

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)
