from django.contrib import admin
from manager.models import Profile, Site, Building, Space

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    model = Site

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    model = Building

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    model = Space