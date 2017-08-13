from django.contrib import admin

from .models import Booking, Contact, Album, Artist


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
        ]
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,]

class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']
