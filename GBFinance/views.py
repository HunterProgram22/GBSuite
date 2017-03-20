from django.shortcuts import render, redirect
from django.views import View
from .forms import MonthBalForm, MonthIncForm
from .models import MonthBal, MonthInc


class Home(View):
    def get(self, request):
        return render(request, 'GBFinance/home.html', {})

class Manage(View):
    def get(self, request):
        return render(request, 'GBFinance/manage.html', {})

class Balance(View):
    def get(self, request):
        month_balance = MonthBal.objects.all().order_by('-date')
        month_balance = month_balance[0:2]
        return render(request, 'GBFinance/balancesheet.html', {'month_balance': month_balance})

class Balance_new(View):
    def post(self, request):
        form = MonthBalForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.save()
            return redirect('GBFinancemanage')
        return render(request, 'GBFinance/balance_edit.html', {'form': form})

    def get(self, request):
        form = MonthBalForm()
        return render(request, 'GBFinance/balance_edit.html', {'form': form})

class Income(View):
    def get(self, request):
        return render(request, 'GBFinance/incomestatement.html', {})

class Income_new(View):
    def post(self, request):
        form = MonthIncForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GBFinancemanage')
        return render(request, 'GBFinance/income_edit.html', {'form': form})
    
    
    def get(self, request):
        form = MonthIncForm()
        return render(request, 'GBFinance/income_edit.html', {'form': form})

class Cash(View):
    def get(self, request):
        return render(request, 'GBFinance/cashflow.html', {})

class Cash_new(View):
    def get(self, request):
        #form = CashflowForm()
        return render(request, 'GBFinance/cash_edit.html', {})
