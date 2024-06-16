from django.contrib import admin
from .models import Product, Category, SubCategory, Brand, Rating, ProductColors

# Define admin classes
class RatingInline(admin.TabularInline):
    model = Rating

class ProductColorsInline(admin.TabularInline):
    model = ProductColors
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'subcategory')
    search_fields = ('name', 'brand', 'category', 'subcategory')
    list_filter = ('name', 'brand', 'category', 'subcategory')
    inlines = [RatingInline, ProductColorsInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)



# Register models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Brand, BrandAdmin)

