from django.db import models
from django.utils import timezone

class CreditCardStatement(models.Model):
    date = models.DateField(default=timezone.now)
    due_date = models.IntegerField(choices=[(i, i) for i in range(1, 32)])
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    additional_income = models.DecimalField(max_digits=10, decimal_places=2)

class Expense(models.Model):
    statement = models.ForeignKey(CreditCardStatement, on_delete=models.CASCADE, related_name='expenses')
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)