from django.db import models


class Artist(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)

    class Meta:
        verbose_name = "artiste"

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField('email', max_length=100)
    name = models.CharField('nom', max_length=200)

    class Meta:
        verbose_name = "prospect"

    def __str__(self):
        return self.name


class Album(models.Model):
    reference = models.IntegerField('référence', null=True)
    created_at = models.DateTimeField('date de création', auto_now_add=True)
    available = models.BooleanField('disponible', default=True)
    title = models.CharField('titre', max_length=200)
    picture = models.TextField("URL de l'image", )
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    class Meta:
        verbose_name = "disque"

    def __str__(self):
        return self.title


class Booking(models.Model):
    created_at = models.DateTimeField("date d'envoi", auto_now_add=True)
    contacted = models.BooleanField('demande traitée ?', default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "réservation"

    def __str__(self):
        return self.contact.name
