# Generated by Django 4.0.4 on 2022-06-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_image_remove_product_rgb_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floatingbutton',
            name='available',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Статус позвоноли'),
        ),
    ]