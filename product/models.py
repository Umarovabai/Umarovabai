from django.core.exceptions import ValidationError
from django.db import models
from pkg_resources import _

COLOR_PALETTE = [
    ('#FA0DF3', 'Purple',),
    ('#000000', 'Black',),
    ('#141EFF', 'Blue',),
    ('#FF0D22', 'Red',),
    ('#00FF00', 'Green',),
    ('#FA7819', 'Brown',),
    ('#F7FA0A', 'Yellow',),
    ('#FFFFFF', 'White',),

]

PRODUCT_COLORS = (
    ('BLACK', 'Black'),
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
    ('BROWN', 'Brown'),
    ('GREEN', 'Green'),
    ('YELLOW', 'Yellow'),
    ('WHITE', 'White'),
    ('PURPLE', 'Purple'),
)

class Category(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='products', blank=True, verbose_name="Фотографии")

    class Meta:
        ordering = ['name']
        verbose_name = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')
    name = models.CharField(max_length=150, verbose_name='Название')
    artikul = models.CharField(max_length=200, verbose_name='Артикул')
    price = models.IntegerField(default=True, null=True, blank=True, verbose_name='Цена')
    old_price = models.IntegerField(default=True, null=True, blank=True, verbose_name='Старая цена')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидки')
    description = models.CharField(blank=True, max_length=1000, verbose_name='Описание')
    size_range = models.CharField(max_length=100, verbose_name='Размерный ряд')
    composition = models.CharField(max_length=100, verbose_name='Состав ткани')
    stock = models.PositiveIntegerField(verbose_name='Количество в линейке')
    material = models.CharField(max_length=100, verbose_name='Материал')
    bestseller = models.BooleanField(default=True, verbose_name='Хит продаж')
    novelties = models.BooleanField(default=True, verbose_name='Новинки')

    class Meta:
        ordering = ['name']
        index_together = ['id']

    def __str__(self):
        return self.name

class ProductItem(models.Model):
    size_range = models.CharField(max_length=100, null=True, blank=True, verbose_name='Размерный ряд')
    quantity_in_line = models.IntegerField(null=True, blank=True, verbose_name='Количество в линейке')
    Product_item = models.ForeignKey(Product, related_name='product_size', on_delete=models.CASCADE)
    # rgbcolor = models.(choices=COLOR_PALETTE)

    # def __str__(self):
    #     return self.rgbcolor


def validate_even(value):
    if value == 2:
        raise ValidationError(_("%(value)s is not an even number"), params={'value': value})

class ProductItemImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item_image')
    image = models.ImageField(upload_to='products', null=True, blank=True, validators=[validate_even])




