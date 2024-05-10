from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # or specify the fields you want to include in the API response

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # or specify the fields you want to include in the API response

class CartSerializer(serializers.Serializer):
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        items_data = []
        for item in obj:
            item_data = {
                'product': item['product'].id,
                'quantity': item['quantity'],
                'price': item['price']
            }
            items_data.append(item_data)
        return items_data

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'