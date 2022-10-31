from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from decouple import config



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
    
    class Meta:
        ordering = ["-name"]

    class Administrators(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        INTERNAL = 'Internal', _('Internal')
        EXTERNAL = 'External', _('External')

    
    class Owner(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        CITY = 'City', _('City')
        METROPOLITAN = 'Metropolitan area', _('Metropolitan area')
        REGION = 'Region', _('Region')
        STATE = 'State', _('Sate')
        PRIVATE = 'Private owner', _('Private owner')

    class Types(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        SCHOOL = 'School', _('School')
        ADMINISTRATION = 'Administration', _('Administration')
        SPORT = 'Sport', _('Sport')
        OFFICE = 'Office', _('Office')
        HOUSING = 'Housing', _('Housing') 

    name = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_build = models.DateField(blank=True, null = True)
    date_purchase = models.DateField(blank=True, null = True)
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    geometrie = models.MultiPolygonField(srid=int(config('SRID')), null = True, blank=True)
    archived = models.BooleanField(blank=True, null = True, default=False)
    administrators = models.CharField(max_length=50, choices=Administrators.choices, blank=True)
    types = models.CharField(max_length=50, choices=Types.choices, null = False)
    owner = models.CharField(max_length=50, choices=Owner.choices, blank=True, null = False)

    def __str__(self):
        return self.name

class Building(models.Model):

    class Meta:
        ordering = ["-name"]

    class Administrators(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        INTERNAL = 'Internal', _('Internal')
        EXTERNAL = 'External', _('External')

    
    class Owner(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        CITY = 'City', _('City')
        METROPOLITAN = 'Metropolitan area', _('Metropolitan area')
        REGION = 'Region', _('Region')
        STATE = 'State', _('Sate')
        PRIVATE = 'Private owner', _('Private owner')

    class Types(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        SCHOOL = 'School', _('School')
        ADMINISTRATION = 'Administration', _('Administration')
        SPORT = 'Sport', _('Sport')
        OFFICE = 'Office', _('Office')
        HOUSING = 'Housing', _('Housing') 

    name = models.CharField(max_length=20, unique=True, null = False)
    street = models.CharField(max_length=255, blank=True)
    date_build = models.DateField(blank=True, null = True)
    date_purchase = models.DateField(blank=True, null = True)
    administrators = models.CharField(max_length=50, choices=Administrators.choices, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    geometrie = models.MultiPolygonField(srid=int(config('SRID')), null = True, blank=True)
    surface_external_work = models.FloatField(blank=True, null = True)
    surface_internal_work = models.FloatField(blank=True, null = True)
    surface_office = models.FloatField(blank=True, null = True)
    surface_rent = models.FloatField(blank=True, null = True)
    surface_floor = models.FloatField(blank=True, null = True)
    surface_under_roof = models.FloatField(blank=True, null = True)
    archived = models.BooleanField(blank=True, null = True, default=False)
    types = models.CharField(max_length=50, choices=Types.choices, null = False)
    owner = models.CharField(max_length=50, choices=Owner.choices, blank=True, null = False)

    def __str__(self):
        return self.name

class Space(models.Model):
    
    class Meta:
        ordering = ["-name"]

    class Administrators(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        INTERNAL = 'Internal', _('Internal')
        EXTERNAL = 'External', _('External')

    
    class Owner(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        CITY = 'City', _('City')
        METROPOLITAN = 'Metropolitan area', _('Metropolitan area')
        REGION = 'Region', _('Region')
        STATE = 'State', _('Sate')
        PRIVATE = 'Private owner', _('Private owner')

    class Types(models.TextChoices):
        EMPTY_LABEL = '', '---------'
        SCHOOL = 'School', _('School')
        ADMINISTRATION = 'Administration', _('Administration')
        SPORT = 'Sport', _('Sport')
        OFFICE = 'Office', _('Office')
        HOUSING = 'Housing', _('Housing') 
    name = models.CharField(max_length=20, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    date_build = models.DateField(blank=True, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_purchase = models.DateField(blank=True, null = True)
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    geometrie = models.MultiPolygonField(srid=int(config('SRID')), null = True, blank=True)
    archived = models.BooleanField(blank=True, null = True, default=False)
    administrators = models.CharField(max_length=50, choices=Administrators.choices, blank=True)
    types = models.CharField(max_length=50, choices=Types.choices, null = False)
    owner = models.CharField(max_length=50, choices=Owner.choices, blank=True, null = False)

    def __str__(self):
        return self.name