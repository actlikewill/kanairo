from django import forms
from .models.category import Category

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = [
            'title'
        ]