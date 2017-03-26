from .models import MonthInc

def report(quarter, year):
    if quarter == "1":
        monthstart = "1"
        monthend = "3"
    elif quarter == "2":
        monthstart = "4"
        monthend = "6"
    elif quarter == "3":
        monthstart = "7"
        monthend = "9"
    elif quarter == "4":
        monthstart = "10"
        monthend = "12"
    year = year
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
    for months in quartermonths:
        creditcards += months.total_creditcards()
        utilities += months.total_utilities()
        loans += months.total_loans()
        savings += months.total_allsavings()
    return (creditcards, utilities, loans, savings)
        