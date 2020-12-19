from django.urls import path
from internet_banking.views import ClientListView, AccountListView, TransactionListView

urlpatterns = [
    path('client/', ClientListView.as_view(), name='client-list'),
    path('account/', AccountListView.as_view(), name='account-list'),
    path('transaction/', TransactionListView.as_view(), name='transaction-list'),
]