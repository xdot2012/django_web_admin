from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from legacy.tasks import task_read
from legacy.models import Sale
from django.views import View


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "templates/home.html")

        else:
            return redirect(reverse_lazy('login'))


def teste(request):
    Sale.objects.all().delete()
    # result = task_read.delay()
    df = task_read()
    Sale.create_from_dataframe(df)
    return render(request, "templates/home.html", {'data': df.to_json()})

