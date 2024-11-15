from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import CreditCardStatement, Expense
from .forms import CreditCardStatementForm, ExpenseForm
from django.db.models import Sum

class HomeView(TemplateView):
    template_name = 'home.html'

def statement_view(request):
    if request.method == 'POST':
        form = CreditCardStatementForm(request.POST)
        if form.is_valid():
            statement = form.save()
            return redirect('statement_detail', pk=statement.pk)
    else:
        form = CreditCardStatementForm()
    
    return render(request, 'statement_form.html', {'form': form})

def statement_detail(request, pk):
    statement = CreditCardStatement.objects.get(pk=pk)
    expenses = statement.expenses.all()
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = statement.account_balance + statement.salary + statement.additional_income - total_expenses

    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.statement = statement
            expense.save()
            return redirect('statement_detail', pk=pk)
    else:
        expense_form = ExpenseForm()

    context = {
        'statement': statement,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'balance': balance,
        'expense_form': expense_form,
    }
    return render(request, 'statement_detail.html', context)

def last_month_statement(request):
    # Criar uma fatura fictícia para o mês passado
    last_month = CreditCardStatement.objects.create(
        due_date=10,
        account_balance=2000,
        salary=1400,
        additional_income=200
    )
    expenses = [
        ('Roupas', 300),
        ('Comida', 500),
        ('Uber', 150),
        ('Ônibus', 100),
        ('Presentes', 200),
        ('Celular', 80),
    ]
    for desc, amount in expenses:
        Expense.objects.create(statement=last_month, description=desc, amount=amount)
    
    return redirect('statement_detail', pk=last_month.pk)