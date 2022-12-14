from django.urls import path

from artista import views

app_name = "artista"
urlpatterns = [
    path("artistas", views.artistas, name="artists-list"),
     path("artist/add", views.create_artist, name="artist-add"),
]