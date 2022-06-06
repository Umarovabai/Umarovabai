from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from product.models import Category, Product, ProductItemImage, Help, About_us, OurAdvantages, PublicOffer, News, Slider


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'

class ProductItemImageInline(admin.TabularInline):
    model = ProductItemImage
    max_num = 8
    min_num = 0

# class ProductItemInline(admin.StackedInline):
#     model = ProductItem
#     fields = ['size_range', 'quantity_in_line', 'Product_item']

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [
        ProductItemImageInline,

    ]


admin.site.register(Category)
admin.site.register(PublicOffer)
admin.site.register(Help)
admin.site.register(About_us)
admin.site.register(OurAdvantages)
admin.site.register(ProductItemImage)
admin.site.register(News)
admin.site.register(Slider)




