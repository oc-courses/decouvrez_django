from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)


class Album(models.Model):
    reference = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.TextField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
