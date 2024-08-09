from django.contrib import admin
from django.urls import include, path, re_path
from main import views

urlpatterns = [
    path('', views.render_html, {'template_name': 'index.html'}, name='index'),
    re_path(r'^(?P<template_name>.+\.html)$', views.render_html, name='render_html'),
    
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'))
]
