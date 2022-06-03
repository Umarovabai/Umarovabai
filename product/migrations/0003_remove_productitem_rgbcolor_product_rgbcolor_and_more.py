# Generated by Django 4.0.4 on 2022-06-03 09:46

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_ouradvantages_alter_about_us_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='rgbcolor',
        ),
        migrations.AddField(
            model_name='product',
            name='rgbcolor',
            field=colorfield.fields.ColorField(choices=[('#FA0DF3', 'Purple'), ('#000000', 'Black'), ('#141EFF', 'Blue'), ('#FF0D22', 'Red'), ('#00FF00', 'Green'), ('#FA7819', 'Brown'), ('#F7FA0A', 'Yellow'), ('#FFFFFF', 'White')], default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='ouradvantages',
            name='image',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='Картинка'),
        ),
    ]
