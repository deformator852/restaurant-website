from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("menu/", MenusListPage.as_view(), name="menu"),
    path("reservation/", ReservationPage.as_view(), name="reservation"),
    path("product/detail/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("contact-us/", ContactPage.as_view(), name="contact-us"),
    path(
        "success-reservation/",
        TemplateView.as_view(template_name="home/reservation-success.html"),
        name="success-reservation",
    ),
    path(
        "success-feedback/",
        TemplateView.as_view(template_name="home/feedback-success.html"),
        name="success-feedback",
    ),
]
