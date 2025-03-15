from django.urls import path
from .views import HomePage, AboutPage, MenusListPage, ProductDetail, ReservationPage

urlpatterns = [
    path("", HomePage.as_view()),
    path("about/", AboutPage.as_view()),
    path("menus-list/", MenusListPage.as_view()),
    path("reservation/", ReservationPage.as_view()),
    path("product/detail/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
]
