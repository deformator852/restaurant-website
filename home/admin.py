from django.contrib import admin
from home.models import Category, Product, Tag

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
