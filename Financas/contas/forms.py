from django import forms
from .models import CreditCardStatement, Expense

class CreditCardStatementForm(forms.ModelForm):
    class Meta:
        model = CreditCardStatement
        fields = ['due_date', 'account_balance', 'salary', 'additional_income']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount']