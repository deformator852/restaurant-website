from django.urls import path
from .views import HomePage, AboutPage

urlpatterns = [path("", HomePage.as_view()), path("about/", AboutPage.as_view())]
