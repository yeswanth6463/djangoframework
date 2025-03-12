from django.contrib import admin
from cbvapp.models import company, product, productimages

# Register your models here.
admin.site.register(company)
admin.site.register(productimages)

class ProductImageInline(admin.TabularInline):
    model = productimages
    extra = 1  # Allows adding multiple images at once

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
admin.site.register(product, ProductAdmin)
