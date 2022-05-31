from django.contrib import admin

from product.models import Category, Product, ProductItemImage, ProductItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductItemImage)
admin.site.register(ProductItem)

