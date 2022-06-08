from decimal import Decimal

from colorfield.fields import ColorField
from django.conf import settings
from django.db import models

from product.models import Product, ProductItem, ProductItemImage


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product', blank=True)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_items', blank=True)
    product_item_image = models.ForeignKey(ProductItemImage, null=True, on_delete=models.CASCADE,
                                           related_name='product_items_'
                                                        'image', blank=True)

    quantity = models.PositiveIntegerField(default=1)
    price_q = models.IntegerField(default=True, null=True, blank=True, verbose_name='Cтоимость')
    quan_sum = models.IntegerField(default=True, null=True, blank=True, verbose_name='Общ Количество линеек:')
    rebate = models.IntegerField(default=True, null=True, blank=True, verbose_name='Скидка')
    sum_r = models.IntegerField(default=True, null=True, blank=True, verbose_name='Итого')

    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True,editable=False, verbose_name='Фотография')
    name = models.CharField(max_length=200, blank=True, null=True,editable=False, verbose_name='Название товара')
    recolor = ColorField(default='#000000', editable=False)
    price1 = models.IntegerField(default=True, null=True, blank=True,editable=False ,verbose_name='Цена')
    old_price = models.IntegerField(default=True, null=True, blank=True,editable=False, verbose_name='Старая цена')




    def save(self, *args, **kwargs):
        self.price_q = self.product.old_price * self.quan_sum
        # print(self.price_q, 'Стоимость всех линеек')
        self.quan_sum = self.product.stock * self.quantity
        # print(self.quan_sum, 'общ кол линеек')
        self.rebate = (self.product.old_price - self.product.price) * self.quan_sum
        # print(self.rebate, 'Скидка')
        self.sum_r = self.product.price * self.quan_sum

        self.price1 = self.product.price
        self.name = self.product.name
        self.old_price = self.product.old_price
        self.image = self.product_item_image.image
        self.recolor = self.product_item_image.rgbcolor

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.product)