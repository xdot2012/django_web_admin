from django.contrib import admin
from django.urls import path, include
from legacy.apis import SalesViewSet 
from rest_framework import routers
from legacy import views

# Api routes
router = routers.DefaultRouter()
router.register(r'sales', SalesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.HomeView.as_view(), name='home'),
    path('teste', views.teste, name='teste'),
]
