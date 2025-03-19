from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("menu/", MenusListPage.as_view(), name="menu"),
    path("reservation/", ReservationPage.as_view(), name="reservation"),
    path("product/detail/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("contact-us/", ContactPage.as_view(), name="contact-us"),
    path("success-reservation/", success_reservation, name="success-reservation"),
    path("success-feedback/", success_feedback, name="success-feedback"),
]
