from django.urls import path

from my_app import views

app_name = "my_app"
urlpatterns = [
    path("countrys", views.countrys, name="country-list"),
    path("country/add", views.create_country, name="country-add"),
]