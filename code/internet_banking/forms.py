from django import forms
from internet_banking.models import Client, Account, Transaction


class ClientForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask':"000.000.000-00"}))
    birthday = forms.DateField(widget=forms.TextInput(attrs={'data-mask':"00/00/0000"}))

    class Meta:
        model = Client
        fields = '__all__'



class AccountForm(forms.ModelForm):
    number = forms.CharField(widget=forms.TextInput(attrs={'data-mask':"0000 0000 0000 0000"}))

    class Meta:
        model = Account
        exclude = ['limit', 'balance']

class TransactionForm(forms.ModelForm):
    value = forms.DecimalField(max_digits=6, min_value=0)

    class Meta:
        model = Transaction
        exclude = ['approved', 'completed', 'date']