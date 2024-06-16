from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=254, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', default=1)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('SubCategory', blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254, unique=True)
    color = models.CharField(max_length=254, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ratings = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.name

