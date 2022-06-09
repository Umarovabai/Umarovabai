# from django.db import models
#
# from product.models import Product, ProductItemImage
#
#
# class Cart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product', blank=True, null=True)
#     stock = models.PositiveIntegerField(null=True, blank=True, verbose_name="Количество в линейке")
#     image = models.ForeignKey(ProductItemImage, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Цвета товара')
#


