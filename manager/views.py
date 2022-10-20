import io
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, FileResponse
from django_user_agents.utils import get_user_agent
from django.core.paginator import Paginator
from reportlab.pdfgen import canvas
from .forms import *

def index(request):
    name = None

    if request.method == "POST":
        name = str(request.POST.get('name'))
        buildings = Building.objects.filter(name__contains = name) #queryset containing all movies we just created
    else : 
        buildings = Building.objects.all() #queryset containing all movies we just created
    user_agent = get_user_agent(request)
    paginator = Paginator(buildings, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    
    if user_agent.is_mobile:
        context = {
            "Sites" : Site.objects.all().order_by('-date_modified'),
            "Buildings" : Building.objects.all(),
            "Spaces" : Space.objects.all().order_by('-date_modified')
        }
        return render(request, "index_mobile.html", context)
    else:
        context = {
            "Sites" : Site.objects.all().order_by('-date_modified'),
            "Buildings" : page_obj,
            "Spaces" : Space.objects.all().order_by('-date_modified'),
            "name": name
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
            raise Http404("This post does not exist")

        if Buildinginstance.geometrie != None : 
            Buildinginstance.geometrie.transform(4326)
        
        context ={
            "Building" : Building.objects.get(id=buildingId),
            "geometrie" : Buildinginstance.geometrie,
            "Spaces" : Space.objects.filter(building = buildingId)
        }
        
        return render(request, "sheet/building_sheet.html", context)

@login_required
def editBuilding(request, buildingId):
    Buildinginstance= Building.objects.get(id=buildingId)
    if request.method == 'POST':
    
        form = BuildingForm(request.POST, request.FILES, instance = Buildinginstance)
  
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BuildingForm(instance = Buildinginstance)
    return render(request, 'edit/building_edit.html', {'form' : form})

@login_required
def addSite(request):
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
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
            return redirect('success')
    else:
        form = SpaceForm()
    return render(request, 'add/space_add.html', {'form' : form})
   
def success(request):
    return HttpResponse('successfully uploaded')