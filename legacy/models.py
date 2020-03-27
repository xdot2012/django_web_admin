from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.


class Venda(models.Model):
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

    @classmethod
    def get_global_sales(self):
        global_sales = self.na_sales + self.eu_sales + self.jp_sales + self.other_sales
        return global_sales

    def __str__(self):
        return self.name
