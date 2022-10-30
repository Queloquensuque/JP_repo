from django.urls import path

from banda import views

app_name = "banda"
urlpatterns = [
    path("bandas", views.bandas, name="bandas-list")
]