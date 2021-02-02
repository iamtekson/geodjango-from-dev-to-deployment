from django.shortcuts import render
from .models import Note


def note(request):
    if(request.method == 'POST'):
        note_heading = request.POST.get('note_heading')
        note_des = request.POST.get('note_des')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        note = Note(note_heading=note_heading, note=note_des, lat=lat, lng=lng)
        note.save()

        return render(request, 'index.html')

    return render(request, 'index.html')
