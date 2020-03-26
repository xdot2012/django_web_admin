from django.shortcuts import render
from legacy.tasks import task_read
from legacy.models import Venda
import pandas as pd
import pandas.io.sql as sql
# Create your views here.


def teste(request):
    lista = Venda.objects.all()
    print(len(lista))
    result = task_read.delay()
    return render(request, "home.html")
