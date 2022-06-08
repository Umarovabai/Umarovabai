from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from product.models import Category, Product, ProductItemImage, Help, About_us, OurAdvantages, PublicOffer, News, \
    Slider, Footer, FloatingButton


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'




class ProductItemImageAdmin(admin.StackedInline):
    model = ProductItemImage
    max_num = 8

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [
        ProductItemImageAdmin,

    ]


admin.site.register(Category)
admin.site.register(PublicOffer)
admin.site.register(Help)
admin.site.register(About_us)
admin.site.register(OurAdvantages)
admin.site.register(News)
admin.site.register(Slider)
admin.site.register(Footer)
admin.site.register(FloatingButton)



