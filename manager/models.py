from django.contrib.gis.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.get_username()


class Site(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Building(models.Model):

    class Meta:
        ordering = ["-name"]

    class Administrators(models.TextChoices):
        GIPB = 'Gestion et Inventaire du Patrimoine Bâti',
        CULTES = 'Cultes'
        SPORT = 'Patrimoine Sportif'

    name = models.CharField(max_length=255, unique=True)
    street = models.CharField(max_length=255, blank=True)
    administrators = models.CharField(max_length=50, choices=Administrators.choices, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    geometrie = models.MultiPolygonField(srid=3948, null = True, blank=True)

    def __str__(self):
        return self.name

class Space(models.Model):
    name = models.CharField(max_length=255, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.name