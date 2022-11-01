from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from banda.forms import BandaForm
from banda.models import Banda


def get_bandas(request):
    bandas = Banda.objects.all()
    return bandas

def bandas(request):
    bandas = Banda.objects.all()

    context_dict = {"bandas": bandas}

    return render(
        request = request,
        context=context_dict,
        template_name="banda/bandas_list.html",
    )

def create_banda(request):
        if request.method == "POST":
            banda_form = BandaForm(request.POST)
            if banda_form.is_valid():
                data = banda_form.cleaned_data
                actual_objects = Banda.objects.filter(
                    name=data['name'], anio=data['anio']
                )
                if actual_objects:
                    messages.error(
                        request,
                        f"La banda {data['name']} - {data['anio']} ya está creada",
                    )
                else:
                    banda = Banda(name=data['name'], anio=data['anio'])
                    banda.save()
                    messages.success(
                        request,
                        f"Banda {data['name']} - {data['anio']} creada exitosamente",
                    )

                return render(
                    request = request,
                    context={"bandas": get_bandas(request)},
                    template_name="banda/bandas_list.html",
                )


        banda_form = BandaForm(request.POST)
        context_dict = {"form": banda_form}
        return render(
            request=request,
            context=context_dict,
            template_name="banda/banda_forms.html",
        )        