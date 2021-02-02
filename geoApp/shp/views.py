from django.shortcuts import render
from .models import Shp
from tiff.models import Tiff
from note.models import Note


def index(request):
    shp = Shp.objects.all()
    tiff = Tiff.objects.all()
    note = Note.objects.all()
    return render(request, 'index.html', {'shp': shp, 'tiff': tiff, 'note': note})


def note(request):
    if(request.method == 'POST'):
        note_heading = request.POST.get('note-heading')
        note = request.POST.get('note')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        print(note_heading, note, lat, lng, 'email username')
        return render(request, 'index.html')
    return render(request, 'index.html')
