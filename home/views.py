

from django.shortcuts import render

from my_app.models import Country

def index(request):

    return render(
        request = request,
        context={},
        template_name="home/index.html",
    )