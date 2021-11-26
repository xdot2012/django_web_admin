from legacy.models import Sale
from rest_framework import serializers


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'rank',
            'name',
            'platform',
            'year',
            'genre',
            'publisher',
            'na_sales',
            'eu_sales',
            'jp_sales',
            'other_sales',
            'changed_by'
        ]