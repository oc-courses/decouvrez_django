import os
import logging as lg

import yaml
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from store.models import Album, Artist


lg.basicConfig(level=lg.DEBUG)


class Command(BaseCommand):
    help = 'Add albums to the database from a yml file located in data/'

    def handle(self, *args, **options):
        reference = 0
        # open file with data
        directory = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(directory, 'data', 'albums.yml')
        with open(path, 'r') as file:
            data = yaml.load(file)
            albums = data['albums']
            for album in albums:
                # Create artists
                artists = []
                for artist in album['artists']:
                    try:
                        stored_artist = Artist.objects.get(name=artist)
                        lg.info('Artist found: %s'%stored_artist)
                    except ObjectDoesNotExist:
                        stored_artist = Artist.objects.create(name=artist)
                        lg.info('Artist created: %s'%stored_artist)
                    artists.append(stored_artist)
                # Find or create album
                try:
                    stored_album = Album.objects.get(title=album['title'])
                    lg.info('Album found: %s'%stored_album.title)
                except ObjectDoesNotExist:
                    reference += 1
                    album = Album.objects.create(
                        title=album['title'],
                        reference=reference,
                        picture=album['picture']
                    )
                    album.artists = artists
                    lg.info('New album: %s'%stored_artist)
