from django.contrib import admin
from .models.category import Category
from .forms import CategoryForm

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['id', 'title']

admin.site.register(Category, CategoryAdmin)
