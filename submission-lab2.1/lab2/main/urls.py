from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.render_html, {'template_name': 'index.html'}, name='index'),
    re_path(r'^(?P<template_name>.+\.html)$', views.render_html, name='render_html'),
]
