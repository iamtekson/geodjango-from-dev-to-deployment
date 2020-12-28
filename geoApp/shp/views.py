from django.shortcuts import render
from .models import Shp


def index(request):
    shp = Shp.objects.all()
    return render(request, 'index.html', {'shp': shp})
