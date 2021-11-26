from rest_framework import viewsets
from legacy.models import Sale
from legacy.serializers import SaleSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer