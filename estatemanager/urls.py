"""estatemanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from manager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('explorer/', include('explorer.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/site', views.addSite, name = 'addSite'),
    path('add/building', views.addBuilding, name = 'addBuilding'),
    path('add/space', views.addSpace, name = 'addSpace'),
    path('success', views.success, name = 'success'),
    path('search', views.search, name = 'search'),
    path("site/<int:siteId>", views.sheetSite, name="sheetSite"),
    path("building/<int:buildingId>", views.sheetBuilding, name="sheetBuilding"),
    path("space/<int:spaceId>", views.sheetSpace, name="sheetSpace"),
    path("site/edit/<int:siteId>", views.editSite, name="editSite"),
    path("building/edit/<int:buildingId>", views.editBuilding, name="editBuilding"),
    path("space/edit/<int:spaceId>", views.editSpace, name="editSpace"),
    path("site/delete/<int:siteId>", views.deleteSite, name="deleteSite"),
    path("building/delete/<int:buildingId>", views.deleteBuilding, name="deleteBuilding"),
    path("space/delete/<int:spaceId>", views.deleteSpace, name="deleteSpace"),
    path('report/<int:buildingId>', views.report, name = 'report'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)