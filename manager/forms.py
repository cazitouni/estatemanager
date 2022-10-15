from django.contrib.gis import forms
from .models import *

class SiteForm(forms.ModelForm):
  
    class Meta:
        model = Site
        fields = ['name', 'author']

class BuildingForm(forms.ModelForm):
  
    class Meta:
        model = Building
        widgets = {
            'geometrie': forms.OSMWidget(attrs={'default_lon' : 7.75290774889795, 'default_lat': 48.5734425944796})
        }
        fields = ['name', 'street', 'administrators', 'author', 'site', 'image', 'geometrie']

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name', 'building', 'author']