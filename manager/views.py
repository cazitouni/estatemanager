from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def index(request):
    context = {
        "Sites" : Site.objects.all().order_by('-date_modified'),
        "Buildings" : Building.objects.all().order_by('-date_modified'),
        "Spaces" : Space.objects.all().order_by('-date_modified')
    }
    return render(request, "index.html", context)

def addSite(request):
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SiteForm()
    return render(request, 'add/site_add.html', {'form' : form})

def addBuilding(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BuildingForm()
    return render(request, 'add/building_add.html', {'form' : form})

def addSpace(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SpaceForm()
    return render(request, 'add/space_add.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')