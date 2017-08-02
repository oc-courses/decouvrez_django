from django.http import HttpResponse
from django.shortcuts import render

from .models import ALBUMS

def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def listing(request):
    albums = [album['name'] for album in ALBUMS]
    message = """
        <ul>
            <li>{}
        </ul>
    """.format("</li><li>".join(albums))
    return HttpResponse(message)
