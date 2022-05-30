from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from product.models import Product, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('Category', 'image', 'name', 'artikul', 'price', 'old_price', 'diskount',
                  'description', 'size_range', 'composition', 'stock', 'material')

class SimilarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'color', 'name', 'price', 'old_price', 'diskount', 'size')


