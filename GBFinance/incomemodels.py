from django.db import models

class MonthInc(models.Model):
    date = models.DateField()
    huntington_interest = models.DecimalField(max_digits=8, decimal_places=2)
    fifththird_interest = models.DecimalField(max_digits=8, decimal_places=2)
    capone_interest = models.DecimalField(max_digits=8, decimal_places=2)
    amex_interest = models.DecimalField(max_digits=8, decimal_places=2)
    schwab_interest = models.DecimalField(max_digits=8, decimal_places=2)
    schwab_dividends = models.DecimalField(max_digits=8, decimal_places=2)
    
    