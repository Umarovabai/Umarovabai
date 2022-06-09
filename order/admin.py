from django.contrib import admin

from order.models import ProductItem, Order


class CartItemInline(admin.TabularInline):
    model = ProductItem
    max_num = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline,

    ]

admin.site.register(Order, OrderAdmin)
