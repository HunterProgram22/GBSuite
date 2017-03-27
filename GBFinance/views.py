from django.shortcuts import render, redirect
from django.views import View
from .forms import MonthBalForm, MonthIncForm
from .models import MonthBal, MonthInc
from .functions import report


class Home(View):
    def get(self, request):
        dash_balance = MonthBal.objects.latest('date')
        dash_income = MonthInc.objects.latest('date')
        return render(request, 'GBFinance/home.html', {'dash_balance': dash_balance,
        'dash_income': dash_income})

class Manage(View):
    def get(self, request):
        return render(request, 'GBFinance/manage.html', {})

class Reports(View):
    def get(self, request):
        return render(request, 'GBFinance/reports.html', {})

    def post(self, request):
        quarter = request.POST.get("quarter")[0]
        year = request.POST.get("quarter")[2:]
        quarter_report = quarter + "Q " + year
        yearago_report = quarter + "Q " + str(int(year)-1)
        currentquarter_report = report(quarter, year)
        if quarter == "1":
            lastquarter = "4"
            lastquarteryear = str(int(year)-1)
        else:
            lastquarter = str(int(quarter)-1)
            lastquarteryear = year
        lastquarter_report = report(lastquarter, lastquarteryear)
        lastquarter_report_name = lastquarter + "Q " + lastquarteryear
        year = str(int(year)-1)
        yearagoquarter_report = report(quarter, year)
        ''' _reports are returned as a tuple in the format (total_creditcards,
        total_utilities, total_loans, total_savings)'''
        return render(request, 'GBFinance/reports.html',
                      {'quarter_report': quarter_report,
                       'lastquarter_report_name': lastquarter_report_name,
                       'yearago_report': yearago_report,
                       'currentquarter_report': currentquarter_report,
                       'lastquarter_report': lastquarter_report,
                       'yearagoquarter_report': yearagoquarter_report})


class Analysis(View):
    def get(self, request):
        send_data=[(0,0)]
        return render(request, 'GBFinance/analysis.html', {'send_data': send_data})

    def post(self, request):
        send_data = []
        year = request.POST.get("year")
        if year == "ALL":
            monthly_data = MonthInc.objects.all()
        else:
            monthly_data = MonthInc.objects.filter(date__year=year)
        category = request.POST.get("category")
        for item in monthly_data:
            month = item.date
            amount = getattr(item, category)
            send_data.append((month, amount))
        return render(request, 'GBFinance/analysis.html', {'send_data': send_data, 'category': category})

class Balance(View):
    def get(self, request):
        month_balance = MonthBal.objects.order_by('-date')[:2]
        return render(request, 'GBFinance/balancesheet.html', {'month_balance': month_balance})

    def post(self, request):
        if request.POST.get("month") != '' and request.POST.get("year") != '':
            month = request.POST.get("month")
            year = request.POST.get("year")
            month_balance = MonthBal.objects.filter(date__month=month).filter(date__year=year)
            month_balance = list(month_balance[:])
            add_month = MonthBal.objects.order_by('-date')[0:1]
            month_balance.append(add_month[0])
        elif request.POST.get("month") != '':
            month = request.POST.get("month")
            month_balance = MonthBal.objects.filter(date__month=month)
        elif request.POST.get("year") != '':
            year = request.POST.get("year")
            month_balance = MonthBal.objects.filter(date__year=year)
        else:
            month_balance = MonthBal.objects.order_by('-date')[:2]
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
        month_income = MonthInc.objects.order_by('-date')[:2]
        return render(request, 'GBFinance/incomestatement.html', {'month_income': month_income})

    def post(self, request):
        if request.POST.get("month") != '' and request.POST.get("year") != '':
            month = request.POST.get("month")
            year = request.POST.get("year")
            month_income = MonthInc.objects.filter(date__month=month).filter(date__year=year)
            month_income = list(month_income[:])
            add_month = MonthInc.objects.order_by('-date')[0:1]
            month_income.append(add_month[0])
        elif request.POST.get("month") != '':
            month = request.POST.get("month")
            month_income = MonthInc.objects.filter(date__month=month)
        elif request.POST.get("year") != '':
            year = request.POST.get("year")
            month_income = MonthInc.objects.filter(date__year=year)
        else:
            month_income = MonthInc.objects.order_by('-date')[:2]
        return render(request, 'GBFinance/incomestatement.html', {'month_income': month_income})

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
        month_cash = MonthInc.objects.all().order_by('-date')
        month_cash = month_cash[0:2]
        return render(request, 'GBFinance/cashflow.html', {'month_cash': month_cash})
