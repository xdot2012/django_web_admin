from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('secure/auth/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("select2/", include("django_select2.urls")),

    #   User Paths
    path('accounts/', include('accounts.urls')),
    path('secure/', include('internet_banking.urls')),
    path('', include('legacy.urls')),
]
