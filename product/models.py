from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(blank=True, verbose_name="Фотографии")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField()
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
    bestceller = models.BooleanField(default=True, verbose_name='Хит продаж')
    novelties = models.BooleanField(default=True, verbose_name='Новинки')

    class Meta:
        ordering = ['name']
        index_together = ['id']

    def __str__(self):
        return self.name



