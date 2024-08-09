from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
 path('login_user', views.login_user, name="login"),
]
