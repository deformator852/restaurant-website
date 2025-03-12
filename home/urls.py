from django.urls import path
from .views import HomePage, AboutPage, MenusListPage, ReservationPage

urlpatterns = [
    path("", HomePage.as_view()),
    path("about/", AboutPage.as_view()),
    path("menus-list/", MenusListPage.as_view()),
    path("reservation/", ReservationPage.as_view()),
]
