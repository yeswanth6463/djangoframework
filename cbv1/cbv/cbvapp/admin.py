from django.contrib import admin
from cbvapp.models import Company,Product,ProductImages

# Register your models
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductImages)
