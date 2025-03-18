from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views import View

from home.forms import FirstReservationForm, SecondReservationForm
from .models import Product


class ContactPage(View):
    def get(self, request):
        context = {}
        return render(request, "home/contact-us.html", context=context)


class ProductDetail(View):
    def get(self, request, pk: int):
        context = {}
        item = get_object_or_404(Product, id=pk)
        context["item"] = item
        context["MEDIA_URL"] = settings.MEDIA_URL
        tags = [tag["name"] for tag in item.tags.all().values("name")]
        tags = ",".join(tags)
        context["item_tags"] = tags
        return render(request, "home/product-detail.html", context=context)


class HomePage(View):
    def get(self, request):
        context = {}
        form = FirstReservationForm()
        popular_dishes = Product.objects.all()[0:3].values(
            "id", "name", "image", "price"
        )
        context["popular_dishes"] = popular_dishes
        context["form"] = form
        return render(request, "home/home.html", context=context)


class AboutPage(View):
    def get(self, request):
        form = FirstReservationForm()
        context = {}
        context["form"] = form
        return render(request, "home/about.html", context=context)


class MenusListPage(View):
    def get(self, request):
        context = {}
        products = Product.objects.all()[0:15].values("id", "name", "image", "price")
        context["products"] = products
        return render(request, "home/menus-list.html", context=context)


class ReservationPage(View):
    def get(self, request):
        form = SecondReservationForm()
        context = {}
        context["form"] = form
        return render(request, "home/reservation.html", context=context)
