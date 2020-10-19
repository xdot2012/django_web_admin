from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from legacy import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('teste', views.teste, name='teste'),
]
