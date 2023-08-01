from django.contrib import admin

from .models import Advert, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    pass
