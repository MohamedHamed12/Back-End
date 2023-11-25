
from rest_framework import serializers

from products.models import Category , Product , Discount


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Discount
        fields = '__all__'
