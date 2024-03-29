"""fullStack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url, include # Add include to the imports here

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pathfinder.urls')), # tell django to read urls.py in example app

    path('admin/', admin.site.urls)
    #path('', include('pathfinder.urls')),
    #path('characterCreator/', include('pathfinder.urls')),
    #path('battleSim/', include('pathfinder.urls')),
    #path('beginnersGuide/', include('pathfinder.urls')),
    #path('info/', include('pathfinder.urls')),
    #path('login/', include('pathfinder.urls'))




]
