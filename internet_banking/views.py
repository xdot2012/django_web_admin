from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from internet_banking.models import Client, Account, Transaction
# Create your views here.


class ClientListView(ListView):
    template_name = "templates/generic/list.html"
    model = Client
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AccountListView(ListView):
    template_name = "templates/generic/list.html"
    model = Account
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TransactionListView(ListView):
    template_name = "templates/generic/list.html"
    model = Transaction
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
