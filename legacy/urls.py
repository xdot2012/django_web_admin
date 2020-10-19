from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from legacy import views

urlpatterns = [
    path('teste', views.teste, name='teste'),
    path('', views.home, name='home'),
]
