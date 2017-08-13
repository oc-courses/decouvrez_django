from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Booking, Contact, Album, Artist


class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % (
            content_type.model),
            args=(obj.id,))


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin, AdminURLMixin):
    list_filter = ['created_at', 'contacted']
    fields = ["created_at", "contact_link", 'album_link', 'contacted']
    readonly_fields = ["created_at", "contact_link", "album_link", "contacted"]

    def has_add_permission(self, request):
        return False

    def contact_link(self, booking):
        url = self.get_admin_url(booking.contact)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))

    def album_link(self, booking):
        url = self.get_admin_url(booking.album)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

class BookingInline(admin.TabularInline, AdminURLMixin):
    model = Booking
    extra = 0
    readonly_fields = ["created_at", "album_link", "contacted"]
    fields = ["created_at", "album_link", "contacted"]
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

    def has_add_permission(self, request):
        return False

    def album_link(self, booking):
        url = self.get_admin_url(booking.album)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    album_link.short_description = "Album"


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
