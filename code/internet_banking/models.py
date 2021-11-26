from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    cpf = models.CharField(max_length=20, verbose_name="CPF", unique=True)
    birthday = models.DateField(verbose_name="Data de nascimento")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Cliente:{self.name} - [{self.cpf}]'


class Account(models.Model):
    client = models.ForeignKey(Client, verbose_name="Cliente", on_delete=models.DO_NOTHING, related_name="accounts")
    number = models.CharField(verbose_name="Numéro", max_length=100, unique=True)
    max_limit = models.DecimalField(verbose_name="Limite Máximo", decimal_places=2, max_digits=10)
    limit = models.DecimalField(verbose_name="Limite", decimal_places=2, max_digits=10, default=0)
    balance = models.DecimalField(verbose_name="Saldo", decimal_places=2, max_digits=10, default=0)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'Conta:[{self.number}] - {self.client.name}'

    def allow_transaction(self, transaction_type, value):
        if transaction_type == 'CR':
            return True
        else:
            if self.balance + (self.max_limit - self.limit) >= value:
                return True
            else:
                return False

    def make_transaction(self, transaction_type, value):
        if transaction_type == 'CR':
            if self.limit == 0:
                self.balance += value
            else:
                self.limit -= value
                if self.limit < 0:
                    self.balance += self.limit * (-1)
                    self.limit = 0
        else:
            self.balance -= value
            if self.balance < 0:
                self.limit += self.balance * (-1)
                self.balance = 0
        self.save()
        return True


class Transaction(models.Model):
    TRANSACTION_TYPES = (('CR', 'Crédito'), ('DR', 'Débito'))
    account = models.ForeignKey(Account, verbose_name="Conta", on_delete=models.DO_NOTHING, related_name="transactions")
    type = models.CharField(verbose_name="Tipo", choices=TRANSACTION_TYPES, max_length=2)
    value = models.DecimalField(verbose_name="Valor", decimal_places=2, max_digits=10)
    approved = models.BooleanField(verbose_name="Approved", default=False)
    completed = models.BooleanField(verbose_name="Completed", default=False)
    date = models.DateTimeField(verbose_name="Data", auto_now=True)

    def save(self):
        if self.account.allow_transaction(self.type, self.value):
            self.approved = True
            self.account.make_transaction(self.type, self.value)
            self.completed = True
        else:
            self.completed = True
        return super(Transaction, self).save()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Transação:[{self.account}] - {self.type}: {self.value}'
