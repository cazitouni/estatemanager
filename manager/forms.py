from django import forms
from .models import *

class SiteForm(forms.ModelForm):
  
    class Meta:
        model = Site
        fields = ['name', 'author']

class BuildingForm(forms.ModelForm):
  
    class Meta:
        model = Building
        fields = ['name', 'street', 'administrators', 'author', 'site', 'image']

class SpaceForm(forms.ModelForm):
  
    class Meta:
        model = Space
        fields = ['name', 'building', 'author']