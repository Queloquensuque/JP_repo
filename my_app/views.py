from django.shortcuts import render

from my_app.models import Country

def countrys(request):
    countrys = Country.objects.all()

    context_dict = {"countrys": countrys}

    return render(
        request = request,
        context=context_dict,
        template_name="my_app/country_list.html",
    )