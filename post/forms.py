from django import forms
from .models import Category
from post.models import Product


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=50)
    image = forms.ImageField(required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    description = forms.CharField(widget=forms.Textarea())


class CategoryCreateForm(forms.Form):
    text = forms.CharField(max_length=60)


class ReviewCreateForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    text = forms.CharField(max_length=70)
