from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'number', 'address', 'introduction', 'photo1', 'photo2', 'photo3']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'photo1']