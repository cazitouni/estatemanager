import io
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django_user_agents.utils import get_user_agent
from django.core.paginator import Paginator
from django.template import Library
from django.urls import reverse
from reportlab.pdfgen import canvas
from .forms import *
from itertools import chain

def search(request): 

    if request.method == "POST" :
        jsonObject = json.dumps(request.POST)
        return JsonResponse({"jsonObject" : jsonObject})
    return None

def index(request):
    
    name = None
    address = None
    types = None
    administrators = None
    owner = None
    build_after = None
    archived = None
    list_addr = []
    
    buildings = []
    paginator = Paginator(buildings, 5)
    form = SearchBuildingForm(request.POST)
    buildings = Building.objects.all().order_by('-date_modified')
    sites = Site.objects.all().order_by('-date_modified')
    spaces = Space.objects.all().order_by('-date_modified')
    user_agent = get_user_agent(request)

    if request.method == "POST":
        
        element = request.POST.get("element")
        name = request.POST.get("name")
        types = request.POST.get("type")
        administrators = request.POST.get("administrators")
        owner = request.POST.get("owner")
        build_after = request.POST.get("build_after")
        archived = request.POST.get("archived")   
        address = request.POST.get("address")   
        
         
        if types != '': 
            buildings = buildings.filter(types__icontains = types)
            sites = sites.filter(types__icontains = types)
            spaces = spaces.filter(types__icontains = types)
        if name != '':
            buildings = buildings.filter(name__icontains = name)
            sites = sites.filter(name__icontains = name)
            spaces = spaces.filter(name__icontains = name)
        if address != '':
            buildings = buildings.filter(street__icontains = address)
            for building in buildings :
                list_addr.append(building.site)
            sites = sites.filter(name__in = list_addr)
            spaces = spaces.filter(building__street__icontains = address)
        if administrators != '':
            buildings = buildings.filter(administrators__icontains = administrators)
            sites = sites.filter(administrators__icontains = administrators)
            spaces = spaces.filter(name__icontains = name)
        if owner != '':
            buildings = buildings.filter(owner__icontains = owner)
            sites = sites.filter(owner__icontains = owner)
            spaces = spaces.filter(owner__icontains = owner)
        if build_after != '':
            buildings = buildings.filter(date_build__gt= build_after)
            sites = sites.filter(date_build__gt = build_after)
            spaces = spaces.filter(date_build__gt = build_after)
        if archived != None:
            buildings = buildings.filter(archived=True)
            sites = sites.filter(archived=True)
            spaces = spaces.filter(archived=True)

        if element == '' or element == None: 
            result_list = list(chain(sites, buildings, spaces))
        if element == 'Site' :
            result_list = sites
        if element == 'Building' :
            result_list = buildings
        if element == 'Space':
            result_list = spaces
            
        paginator = Paginator(result_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        get_request = False      
    else : 
        page_number = request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        get_request = True
        

    context = {
        "Sites" : Site.objects.all().order_by('-date_modified'),
        "Buildings" : page_obj,
        "Spaces" : Space.objects.all().order_by('-date_modified'),
        "name": name,
        "address": address,
        "type" : types,
        "administrators" : administrators,
        "owner" : owner,
        "build_after" : build_after,
        "archived" : archived,
        "form" : form,
        "get_request" : get_request
    }
    return render(request, "index.html", context)
 
def report(request, buildingId):

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def sheetBuilding(request, buildingId):

    if request.method == "GET":

        try:
            Buildinginstance= Building.objects.get(id=buildingId)
            
        except Building.DoesNotExist:
            raise Http404("This Building does not exist")

        if Buildinginstance.geometrie != None : 
            Buildinginstance.geometrie.transform(4326)
        
        context ={
            "Building" : Building.objects.get(id=buildingId),
            "geometrie" : Buildinginstance.geometrie,
            "Spaces" : Space.objects.filter(building = buildingId)
        }
        
        return render(request, "sheet/building_sheet.html", context)
    
def sheetSite(request, siteId):

    if request.method == "GET":

        try:
            siteinstance= Site.objects.get(id=siteId)
            
        except Building.DoesNotExist:
            raise Http404("This Site does not exist")

        if siteinstance.geometrie != None : 
            siteinstance.geometrie.transform(4326)
        
        context ={
            "Site" : siteinstance,
            "geometrie" : siteinstance.geometrie,
            "Buildings" : Building.objects.filter(site = siteId)
        }
        
        return render(request, "sheet/site_sheet.html", context)

def sheetSpace(request, spaceId):

    if request.method == "GET":

        try:
            spaceinstance= Space.objects.get(id=spaceId)
            
        except Building.DoesNotExist:
            raise Http404("This Space does not exist")

        if spaceinstance.geometrie != None : 
            spaceinstance.geometrie.transform(4326)
        
        context ={
            "Space" : spaceinstance,
            "geometrie" : spaceinstance.geometrie,
        }
        
        return render(request, "sheet/space_sheet.html", context)

@login_required
@permission_required('manager.change_site')
def editSite(request, siteId):
    
    siteInstance = Site.objects.get(id=siteId)
    
    if request.method == 'POST':
    
        form = SiteForm(request.POST, request.FILES, instance = siteInstance)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'Site sucessfully modified')
            return redirect('index')
    else:
        form = SiteForm(instance = siteInstance)
    return render(request, 'edit/site_edit.html', {'form' : form})

@login_required
@permission_required('manager.change_building')
def editBuilding(request, buildingId):
    
    buildingInstance= Building.objects.get(id=buildingId)
    
    if request.method == 'POST':
    
        form = BuildingForm(request.POST, request.FILES, instance = buildingInstance)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'Building sucessfully modified')
            return redirect('index')
    else:
        form = BuildingForm(instance = buildingInstance)
    return render(request, 'edit/building_edit.html', {'form' : form})

@login_required
@permission_required('manager.change_space')
def editSpace(request, spaceId):
    
    spaceInstance = Space.objects.get(id=spaceId)
    
    if request.method == 'POST':
    
        form = SpaceForm(request.POST, request.FILES, instance = spaceInstance)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'Space sucessfully modified')
            return redirect('index')
    else:
        form = SpaceForm(instance = spaceInstance)
    return render(request, 'edit/space_edit.html', {'form' : form})

@login_required
@permission_required('manager.delete_site')
def deleteSite(request, siteId):  
   Site.objects.filter(id=siteId).delete()
   messages.success(request, 'Site sucessfully removed')
   return redirect('/')

@login_required
@permission_required('manager.delete_building')
def deleteBuilding(request, buildingId):
   Building.objects.filter(id=buildingId).delete()
   messages.success(request, 'Building sucessfully removed')
   return redirect('/')

@login_required
@permission_required('manager.delete_space')
def deleteSpace(request, spaceId):
   Building.objects.filter(id=spaceId).delete()
   messages.success(request, 'Space sucessfully removed')
   return redirect('/')

@login_required
def addSite(request):
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'Site sucessfully added')
            return redirect('index')
    else:
        form = SiteForm()
    return render(request, 'add/site_add.html', {'form' : form})

@login_required
def addBuilding(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'Building sucessfully added')
            return redirect('/')
    else:
        form = BuildingForm()
    return render(request, 'add/building_add.html', {'form' : form})

@login_required
def addSpace(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'Space sucessfully added')
            return redirect('/')
    else:
        form = SpaceForm()
    return render(request, 'add/space_add.html', {'form' : form})
   
def success(request):
    return HttpResponse('successfully uploaded')