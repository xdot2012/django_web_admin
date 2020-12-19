from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView, CreateView
from meuapp.util import get_model_fields
from internet_banking.models import Client, Account, Transaction
from internet_banking.forms import ClientForm, AccountForm, TransactionForm
# Create your views here.


class ClientListView(ListView):
    template_name = "templates/generic/list.html"
    model = Client
    title = "Cliente"
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        context['columns'] = get_model_fields(self.model)
        context['item_list'] = list(self.object_list.values_list())
        context['create_url'] = 'client-create'
        return context


class ClientCreateView(CreateView):
    form_class = ClientForm
    template_name = "templates/generic/create.html"
    success_url = 'client-list'

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('client-list'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = 'client-create'
        context['return_url'] = 'client-list'
        return context


class AccountListView(ListView):
    template_name = "templates/generic/list.html"
    model = Account
    title = "Conta"
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        context['columns'] = get_model_fields(self.model)
        context['item_list'] = self.object_list.values_list()
        context['create_url'] = 'account-create'
        return context


class AccountCreateView(CreateView):
    form_class = AccountForm
    template_name = "templates/generic/create.html"
    success_url = 'account-list'

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('account-list'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = 'account-create'
        context['return_url'] = 'account-list'
        return context


class TransactionListView(ListView):
    template_name = "templates/generic/list.html"
    model = Transaction
    title = "Transação"
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        context['columns'] = get_model_fields(self.model)
        context['item_list'] = self.object_list.values_list()
        context['create_url'] = 'transaction-create'
        return context


class TransactionCreateView(CreateView):
    form_class = TransactionForm
    template_name = "templates/generic/create.html"
    success_url = 'transaction-list'

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('transaction-list'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = 'transaction-create'
        context['return_url'] = 'transaction-list'
        return context
