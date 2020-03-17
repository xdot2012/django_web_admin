from django.db import models

# Create your models here.


class Venda(models.Model):

    rank = models.IntegerField("Rank")
    name = models.CharField("Name", max_length=30)
    platform = models.CharField("Platform", max_length=30)
    year = models.IntegerField("Year")
    genre = models.CharField("Gênero", max_length=30)
    publisher = models.CharField("Publisher", max_length=50)
    na_sales = models.DecimalField("NA Sales", decimal_places=2, max_digits=2)
    eu_sales = models.DecimalField("EU Sales", decimal_places=2, max_digits=2)
    jp_sales = models.DecimalField("JP Sales", decimal_places=2, max_digits=2)
    other_sales = models.DecimalField(
        "Other Sales", decimal_places=2, max_digits=2)

    @classmethod
    def get_global_sales(self):
        global_sales = self.na_sales + self.eu_sales + self.jp_sales + self.other_sales
        return global_sales

    def __str__(self):
        return self.name
