from .tasks import send_email_for_reservation, send_client_feedback
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .services import create_client_feedback_message, create_reserve_table_message
from .forms import ContactForm, ReservationForm, SecondReservationForm
from .models import Product


class ContactPage(View):
    def get(self, request):
        context = {}
        form = ContactForm()
        context["form"] = form
        return render(request, "home/contact-us.html", context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            message = create_client_feedback_message(form.cleaned_data)
            send_client_feedback.delay(message)  # pyright:ignore
            return redirect("success-feedback")
        context = {}
        context["form"] = form
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
        form = ReservationForm()
        popular_dishes = Product.objects.all()[0:3].values(
            "id", "name", "image", "price"
        )
        context["popular_dishes"] = popular_dishes
        context["form"] = form
        return render(request, "home/home.html", context=context)

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            message = create_reserve_table_message(form.cleaned_data)
            send_email_for_reservation.delay(message)  # pyright:ignore
            return redirect("success-reservation")
        context = {}
        context["form"] = form
        popular_dishes = Product.objects.all()[0:3].values(
            "id", "name", "image", "price"
        )
        context["popular_dishes"] = popular_dishes
        return render(request, "home/home.html", context=context)


class AboutPage(View):
    def get(self, request):
        form = ReservationForm()
        context = {}
        context["form"] = form
        return render(request, "home/about.html", context=context)

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            message = create_reserve_table_message(form.cleaned_data)
            send_email_for_reservation.delay(message)  # pyright:ignore
            return redirect("success-reservation")
        form = ReservationForm()
        context = {}
        context["form"] = form
        return render(request, "home/about.html", context=context)


class MenusListPage(View):
    def get(self, request):
        context = {}
        products_list = Product.objects.all().values("id", "name", "image", "price")
        paginator = Paginator(products_list, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        return render(request, "home/menus-list.html", context=context)

    def post(self, request):
        context = {}
        query = request.POST.get("query", "")

        if query:
            products_list = Product.objects.filter(name__icontains=query).values(
                "id", "name", "image", "price"
            )
        else:
            products_list = Product.objects.all().values("id", "name", "image", "price")

        paginator = Paginator(products_list, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["query"] = query

        return render(request, "home/menus-list.html", context)


class ReservationPage(View):
    def get(self, request):
        form = SecondReservationForm()
        context = {}
        context["form"] = form
        return render(request, "home/reservation.html", context=context)

    def post(self, request):
        form = SecondReservationForm(request.POST)
        if form.is_valid():
            message = create_reserve_table_message(form.cleaned_data)
            send_email_for_reservation.delay(message)  # pyright:ignore
            return redirect("success-reservation")
        return render(request, "home/reservation.html", {"form": form})


def success_reservation(request):
    return render(request, "home/reservation-success.html")


def success_feedback(request):
    return render(request, "home/feedback-success.html")
