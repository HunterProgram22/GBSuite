from django.shortcuts import render, redirect
from .forms import MonthBalForm
from .models import MonthBal

def home(request):
    return render(request, 'GBFinance/home.html', {})

def manage(request):
    return render(request, 'GBFinance/manage.html', {})

def balance(request):
    month_balance = MonthBal.objects.all().order_by('-date')
    month_balance = month_balance[0:3]
    return render(request, 'GBFinance/balancesheet.html', {'month_balance': month_balance})

def balance_new(request):
    if request.method == "POST":
        form = MonthBalForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.save()
            return redirect('/')
    else:
        form = MonthBalForm()
    return render(request, 'GBFinance/balance_edit.html', {'form': form})

def income(request):
    return render(request, 'GBFinance/incomestatement.html', {})

def income_new(request):
    #form = IncStateForm()
    return render(request, 'GBFinance/income_edit.html', {})

def cash(request):
    return render(request, 'GBFinance/cashflow.html', {})

def cash_new(request):
    #form = CashflowForm()
    return render(request, 'GBFinance/cash_edit.html', {})
