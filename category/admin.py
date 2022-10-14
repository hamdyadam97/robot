from django.contrib import admin

# Register your models here.
from category.models import Category, Product,ImageProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ImageProduct)