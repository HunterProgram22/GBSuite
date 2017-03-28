from .models import MonthInc, MonthBal

def report(quarter, year):
    year = year
    yearbal = year
    if quarter == "1":
        monthstart = "1"
        monthend = "3"
        monthbal = "4"
    elif quarter == "2":
        monthstart = "4"
        monthend = "6"
        monthbal="7"
    elif quarter == "3":
        monthstart = "7"
        monthend = "9"
        monthbal = "10"
    elif quarter == "4":
        monthstart = "10"
        monthend = "12"
        monthbal = "1"
        yearbal = str(int(year)+1)
    start_date = monthstart
    end_date = monthend
    print(start_date, end_date)
    quartermonths = MonthInc.objects.filter(date__year=year).filter(
        date__month__gte=monthstart, date__month__lte=monthend)
    print(quartermonths)
    creditcards = 0
    utilities = 0
    loans = 0
    savings = 0
    surplus = 0
    for months in quartermonths:
        creditcards += months.total_personal_creditcards()
        utilities += months.total_utilities()
        loans += months.total_loans()
        savings += months.total_allsavings()
        surplus += months.total_surplus()
    try:
        quarter_end = MonthBal.objects.filter(date__year=yearbal).filter(date__month=monthbal)
        networth = quarter_end[0].networth()
        loanbalance = quarter_end[0].total_loan()
        savingsbalance = quarter_end[0].total_save()
    except IndexError:
        quarter_end = MonthBal.objects.filter(date__year=yearbal).filter(date__month=monthend)
        networth = quarter_end[0].networth()
        loanbalance = quarter_end[0].total_loan()
        savingsbalance = quarter_end[0].total_save()
    return (creditcards, utilities, loans, savings, surplus, networth, loanbalance, savingsbalance)
