from rest_framework import serializers

from product.models import Product, Category, ProductItem, ProductItemImage, About_us, Help_image, Help, OurAdvantages, \
    PublicOffer


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
        fields = ('category', 'image', 'name', 'artikul', 'price', 'old_price', 'diskount',
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
        fields = ('id', 'products', 'name', 'image')


class AboutUsSerializer(serializers.Serializer):
    class Meta:
        model = About_us
        fields = '__all__'

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['question', 'answer']

class Help_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help_image
        fields = ['image_help']

class OurAdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        fields = ('title', 'description', 'image')

class PublicOfferSerializer(serializers.Serializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'






