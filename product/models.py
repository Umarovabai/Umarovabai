from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from colorfield.fields import ColorField
from singleton_model import SingletonModel

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
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='products', blank=True, verbose_name="Картинка")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категории')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')
    rgbcolor = ColorField(choices=COLOR_PALETTE, verbose_name='Выбор цветов')
    name = models.CharField(max_length=150, verbose_name='Название')
    artikul = models.CharField(max_length=200, verbose_name='Артикул')
    price = models.IntegerField(default=True, null=True, verbose_name='Цена')
    old_price = models.IntegerField(default=True, null=True, verbose_name='Старая цена')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидки')
    description = RichTextField(verbose_name='Описание')
    size_range = models.CharField(max_length=100, verbose_name='Размерный ряд')
    composition = models.CharField(max_length=100, verbose_name='Состав ткани')
    stock = models.PositiveIntegerField(verbose_name='Количество в линейке')
    material = models.CharField(max_length=100, verbose_name='Материал')
    bestseller = models.BooleanField(default=True, verbose_name='Хит продаж')
    novelties = models.BooleanField(default=True, verbose_name='Новинки')

    class Meta:
        ordering = ['name']
        index_together = ['id']
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name

class ProductItem(models.Model):
    size_range = models.CharField(max_length=100, null=True, blank=True, verbose_name='Размерный ряд')
    quantity_in_line = models.IntegerField(null=True, blank=True, verbose_name='Количество в линейке')
    Product_item = models.ForeignKey(Product, related_name='product_size', on_delete=models.CASCADE)


    def __str__(self):
        return self.rgbcolor


def validate_even(value):
    if value == 2:
        raise ValidationError(("%(value)s is not an even number"), params={'value': value})

class ProductItemImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item_image')
    image = models.ImageField(upload_to='products', null=True, blank=True, validators=[validate_even])

list_about = []
class About_us(SingletonModel):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = RichTextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')

    class Meta:
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title
#
# class about_us_image(SingletonModel):
#     image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')
#     about = models.ForeignKey(About_us, on_delete=models.CASCADE, related_name='about')


list_help = []
class Help(models.Model):
    question = models.TextField(max_length=200, db_index=True, verbose_name='Вопросы')
    answer = models.TextField(max_length=200, db_index=True, verbose_name='Ответы')

    class Meta:
        verbose_name_plural = 'Помощь'

    def __str__(self):
        return self.question

class Help_image(SingletonModel):
    image_help = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')


    def clean(self):
        list_help.append(len(Help_image.objects.filter(image_help=self.pk)))
        dd = len(list_help)
        print(len(list_help))
        if dd >= 2:
            list_help.clear()
            raise ValidationError('Не больше 1 Фотографий')


class OurAdvantages(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Наши преимущества'

    def __str__(self):
        return self.title

class PublicOffer(SingletonModel):
    name = models.CharField(max_length=300, verbose_name='Заголовок')
    description = RichTextField(null=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Публичная офферта'

    def __str__(self):
        return self.name





















