from django.contrib import admin
from .models import Product, Category, SubCategory

# Define admin classes
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'subcategory')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

# Register models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)