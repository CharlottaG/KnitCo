from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Sub categories'


    name = models.CharField(max_length=254, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', default=1)

    def __str__(self):
        return self.name

class Brand(models.Model):

    name = models.CharField(max_length=254, unique=True)
    website =  models.URLField(null=True, blank=True)
    location = models.CharField(max_length=254, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=254, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('SubCategory', blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return ratings.aggregate(models.Avg('score'))['score__avg']
        return None

class ProductColors(models.Model):

    class Meta:
        verbose_name_plural = 'Product Colors'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_colors')
    color = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} - {self.color}'

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.score} by {self.user.username}'






