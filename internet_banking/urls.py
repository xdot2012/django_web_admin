from django.urls import path
from internet_banking.views import ClientListView, AccountListView, TransactionListView, ClientCreateView, AccountCreateView, TransactionCreateView

urlpatterns = [
    path('client/', ClientListView.as_view(), name='client-list'),
    path('client_create/', ClientCreateView.as_view(), name='client-create'),
    path('account/', AccountListView.as_view(), name='account-list'),
    path('account_create/', AccountCreateView.as_view(), name='account-create'),
    path('transaction/', TransactionListView.as_view(), name='transaction-list'),
    path('transaction_create/', TransactionCreateView.as_view(), name='transaction-create'),
]