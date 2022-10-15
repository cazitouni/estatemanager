from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import *

def index(request):
    context = {
        "Sites" : Site.objects.all().order_by('-date_modified'),
        "Buildings" : Building.objects.all().order_by('-date_modified'),
        "Spaces" : Space.objects.all().order_by('-date_modified')
    }
    return render(request, "index.html", context)

def sheetBuilding(request, buildingId):

    if request.method == "GET":

        try:
            Buildinginstance= Building.objects.get(id=buildingId)
            
        except Building.DoesNotExist:
            raise Http404("This post does not exist")

        if Buildinginstance.geometrie != None : 
            Buildinginstance.geometrie.transform(4326)
        
        context ={
            "Building" : Building.objects.get(id=buildingId),
            "geometrie" : Buildinginstance.geometrie,
        }
        
        return render(request, "sheet/building_sheet.html", context)


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