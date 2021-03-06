"""backendLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views #importing the views file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('f1', views.index, name='index'),
    path('about', views.about, name='about') #name chai path ko nam ho, ani views.about vaneko chai views.py vanne file ma define gareko about function lai represent gareko ho
]

#Laying the pipeline

#urlpatterns = [
#   path('', views.index, name='index'),
#    path('removepunc', views.removepunc, name='rempun'),
#    path('capitalizarfirst', views.capfirst, name='capfirst'),
#    path('newlineremove', views.newlineremove, name='newlineremove'),
#    path('spaceremove', views.spaceremove, name='spaceremove'),
#    path('charcounter', views.charcounter, name='charcount'),
#]

#video 11 backend coding

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
]
