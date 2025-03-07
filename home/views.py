from django.shortcuts import render
from django.views import View
from .models import Product


class Home(View):
    def get(self, request):
        context = {}
        popular_dishes = Product.objects.all()[0:3].values("name", "image", "price")
        context["popular_dishes"] = popular_dishes
        print(popular_dishes)
        return render(request, "home/home.html", context=context)
