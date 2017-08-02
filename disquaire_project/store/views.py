from django.http import HttpResponse
from django.shortcuts import render

from .models import ARTISTS


def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def listing(request):
    artists = [artist['name'] for (key, artist) in ARTISTS.items()]
    return HttpResponse(artists)

def detail(request, album_id):
    pass
