from django import forms
from .models import Rating
from .models import Product, Category

class RatingForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ('score','comment')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # Include all fields from Product model
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
