from rest_framework import serializers

from product.models import Product, Category, ProductItem, ProductItemImage


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('size_range', 'quantity_in_line', 'rgbcolor')

class ProductItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItemImage
        fields = ('image', )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        product_item_image = ProductItemImageSerializer(many=True, read_only=True)
        product_size = ProductItemSerializer(many=True, read_only=True)
        model = Product
        fields = ('Category', 'image', 'name', 'artikul', 'price', 'old_price', 'diskount',
                  'description', 'size_range', 'composition', 'stock', 'material')

class SimilarProductSerializer(serializers.ModelSerializer):
    class Meta:
        product_item_image = ProductItemImageSerializer(many=True, read_only=True)
        product_size = ProductItemSerializer(many=True, read_only=True)
        model = Product
        fields = ('id', 'image', 'color', 'name', 'price', 'old_price', 'diskount', 'size')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


