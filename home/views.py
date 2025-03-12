from django.shortcuts import render
from django.views import View
from .models import Product


class HomePage(View):
    def get(self, request):
        context = {}
        popular_dishes = Product.objects.all()[0:3].values("name", "image", "price")
        context["popular_dishes"] = popular_dishes
        return render(request, "home/home.html", context=context)


class AboutPage(View):
    def get(self, request):
        context = {}
        return render(request, "home/about.html", context=context)


class MenusListPage(View):
    def get(self, request):
        context = {}
        products = Product.objects.all()[0:15].values("name", "image", "price")
        context["products"] = products
        return render(request, "home/menus-list.html", context=context)


class ReservationPage(View):
    def get(self, request):
        context = {}
        return render(request, "home/reservation.html", context=context)
