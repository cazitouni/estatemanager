from django.contrib.gis import forms
from .models import *

class SiteForm(forms.ModelForm):
  
    class Meta:
        model = Site
        exclude = ('archived',)
        fields = '__all__'
        widgets = {
            'geometrie': forms.OSMWidget(attrs={'default_lon' : 7.75290774889795, 'default_lat': 48.5734425944796}),
            'date_build': forms.DateInput(attrs={'type': 'date'}),
            'date_purchase': forms.DateInput(attrs={'type': 'date'})
        }

class BuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        exclude = ('archived',)
        widgets = {
            'geometrie': forms.OSMWidget(attrs={'default_lon' : 7.75290774889795, 'default_lat': 48.5734425944796}),
            'date_build': forms.DateInput(attrs={'type': 'date'}),
            'date_purchase': forms.DateInput(attrs={'type': 'date'})
        }
        fields = '__all__'

class SearchBuildingForm(forms.Form):
    
    name = forms.CharField(label='Name', max_length=100, required=False)
    type = forms.ChoiceField(label='Type', choices=Building.Types.choices, required=False)
    administrators = forms.ChoiceField(label='Administrators', choices=Building.Administrators.choices, required=False)
    owner = forms.ChoiceField(label='Owner', choices=Building.Owner.choices, required=False)
    build_after = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Built after', required=False)
    archived = forms.BooleanField(label='Is Archived', required=False)
    


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        exclude = ('archived',)
        fields = '__all__'
        widgets = {
            'geometrie': forms.OSMWidget(attrs={'default_lon' : 7.75290774889795, 'default_lat': 48.5734425944796}),
            'date_purchase': forms.DateInput(attrs={'type': 'date'})
        }

