from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from artista.models import Artista
from artista.forms import ArtistForm


def get_artists(request):
    artists = Artista.objects.all()
    return artists


def artistas(request):
    artistas = Artista.objects.all()

    context_dict = {"artistas": artistas}

    return render(
        request = request,
        context=context_dict,
        template_name="artista/artist_list.html",
    )


def create_artist(request):
    if request.method == "POST":
        artist_form = ArtistForm(request.POST)
        if artist_form.is_valid():
            data = artist_form.cleaned_data
            actual_objects = Artista.objects.filter(
                name=data['name'], anio=data['anio']
            )
            if actual_objects:
                messages.error(
                    request,
                    f"El artista {data['name']} - {data['anio']} ya está creado",
                )
            else:
                artist = Artista(name=data['name'], anio=data['anio'])
                artist.save()
                messages.success(
                    request,
                    f"El artista {data['name']} - {data['anio']} fue creado exitosamente",
                )

            return render(
                request = request,
                context={"artists": get_artists(request)},
                template_name="artista/artist_list.html",
            )


    artist_form = ArtistForm(request.POST)
    context_dict = {"form": artist_form}
    return render(
        request=request,
        context=context_dict,
        template_name="artista/artist_form.html",
    )        
            