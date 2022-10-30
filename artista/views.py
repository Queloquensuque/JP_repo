from django.shortcuts import render

from artista.models import Artista

def artistas(request):
    artistas = Artista.objects.all()

    context_dict = {"artistas": artistas}

    return render(
        request = request,
        context=context_dict,
        template_name="artista/artist_list.html",
    )