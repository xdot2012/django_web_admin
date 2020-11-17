from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from simple_history.models import HistoricalRecords
import pandas as pd

# Create your models here.

class Sale(models.Model):
    rank = models.IntegerField("Rank")
    name = models.CharField("Name", max_length=300)
    platform = models.CharField("Platform", max_length=50)
    year = models.IntegerField("Year")
    genre = models.CharField("Gênero", max_length=50)
    publisher = models.CharField("Publisher", max_length=50)
    na_sales = models.FloatField("NA Sales")
    eu_sales = models.FloatField("EU Sales")
    jp_sales = models.FloatField("JP Sales")
    other_sales = models.FloatField("Other Sales")
    changed_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
        
    @classmethod
    def get_global_sales(self):
        global_sales = self.na_sales + self.eu_sales + self.jp_sales + self.other_sales
        return global_sales

    @classmethod
    def create_from_dataframe(cls, df):
        my_list = []
        for x in df.T.to_dict().values():
            my_list.append(cls(**x))
        
        cls.objects.bulk_create(my_list)

    def __str__(self):
        return self.name

    @classmethod
    def get_df(cls):
        qs = cls.objects.filter()
        df = pd.DataFrame()
        if(qs.exists()):
            df = pd.DataFrame.from_records(qs.values('rank', 'name', 'platform', 'year', 'genre', 'publisher', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales'))
            df[['name', 'publisher', 'genre']] = df[['name', 'publisher', 'genre']].astype(str)
            df[['rank', 'year']] = df[['rank', 'year']].astype(int)
            df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].astype(float).round(2)
        
        return df
        