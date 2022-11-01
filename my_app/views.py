from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from my_app.models import Country
from my_app.forms import CountryForm
from my_app.models import Country


def get_countrys(request):
    countrys = Country.objects.all()
    return countrys
    


def countrys(request):
    countrys = Country.objects.all()
    context_dict = {"countrys": countrys}
    return render(
        request = request,
        context=context_dict,
        template_name="my_app/country_list.html",
    )

def create_country(request):
    if request.method == "POST":
        country_form = CountryForm(request.POST)
        if country_form.is_valid():
            data = country_form.cleaned_data
            actual_objects = Country.objects.filter(
                name=data['name'], capital=data['capital']
            )
            if actual_objects:
                messages.error(
                    request,
                    f"El pais {data['name']} - {data['capital']} ya está creado",
                )
            else:
                country = Country(name=data["name"], capital=data["capital"])
                country.save()
                messages.success(
                    request,
                    f"País {data['name']} - {data['capital']} creado exitosamente",
                )

            return render(
                request = request,
                context={"countrys": get_countrys(request)},
                template_name="my_app/country_list.html",
            )


    country_form = CountryForm(request.POST)
    context_dict = {"form": country_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/country_form.html",
    )        
        