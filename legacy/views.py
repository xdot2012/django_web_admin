from django.shortcuts import render
from legacy.tasks import task_read

import pandas as pd
import pandas.io.sql as sql
# Create your views here.


def teste(request):
    df = task_read.delay()
    print(type(df))
    return render(request, "home.html")
