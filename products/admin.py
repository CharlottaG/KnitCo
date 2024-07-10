from django.contrib import admin
from .models import Product, Category, SubCategory, Brand, Rating


class RatingInline(admin.TabularInline):
    model = Rating


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'subcategory')
    search_fields = ('name', 'brand', 'category', 'subcategory')
    list_filter = ('name', 'brand', 'category', 'subcategory')
    inlines = [RatingInline]


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

