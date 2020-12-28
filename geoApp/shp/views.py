from django.shortcuts import render
from .models import Shp
from tiff.models import Tiff


def index(request):
    shp = Shp.objects.all()
    tiff = Tiff.objects.all()
    return render(request, 'index.html', {'shp': shp, 'tiff': tiff})
