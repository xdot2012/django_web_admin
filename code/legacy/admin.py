from django.contrib import admin
from import_export import resources
from legacy.models import Sale

# Register your models here.

class SaleResource(resources.ModelResource):

    class Meta:
        model = Sale

admin.site.register(Sale)