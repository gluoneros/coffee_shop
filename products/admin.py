from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "available", "created_at", "updated_at"]
    list_filter = ["available", "created_at", "updated_at"]
    search_fields = ["name", "price", "available"]


admin.site.register(Product, ProductAdmin)
