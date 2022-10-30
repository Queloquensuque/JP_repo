from django.shortcuts import render

from banda.models import Banda

def bandas(request):
    bandas = Banda.objects.all()

    context_dict = {"bandas": bandas}

    return render(
        request = request,
        context=context_dict,
        template_name="banda/bandas_list.html",
    )