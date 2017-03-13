from django.db import models

class MonthBal(models.Model):
        date = models.DateField()
        fifththird_check = models.DecimalField(max_digits=8, decimal_places=2)
        huntington_check = models.DecimalField(max_digits=8, decimal_places=2)
        fifththird_save = models.DecimalField(max_digits=8, decimal_places=2)
        huntington_save = models.DecimalField(max_digits=8, decimal_places=2)
        capone_save = models.DecimalField(max_digits=8, decimal_places=2)
        amex_save = models.DecimalField(max_digits=8, decimal_places=2)
        buckeye_invest = models.DecimalField(max_digits=8, decimal_places=2)
        deacon_invest = models.DecimalField(max_digits=8, decimal_places=2)
        four57_retire = models.DecimalField(max_digits=8, decimal_places=2)
        four01_retire= models.DecimalField(max_digits=8, decimal_places=2)
        roth_retire = models.DecimalField(max_digits=8, decimal_places=2)
        opers_retire = models.DecimalField(max_digits=8, decimal_places=2)
        justin_car= models.DecimalField(max_digits=8, decimal_places=2)
        kat_car = models.DecimalField(max_digits=8, decimal_places=2)
        main_home= models.DecimalField(max_digits=8, decimal_places=2)
        car_loan= models.DecimalField(max_digits=8, decimal_places=2)
        pubstudent_loan = models.DecimalField(max_digits=8, decimal_places=2)
        privstudent_loan= models.DecimalField(max_digits=8, decimal_places=2)
        main_mortgage = models.DecimalField(max_digits=8, decimal_places=2)
        amex_credit = models.DecimalField(max_digits=8, decimal_places=2)
        discover_credit = models.DecimalField(max_digits=8, decimal_places=2)
        capone_credit = models.DecimalField(max_digits=8, decimal_places=2)
        
        def __str__(self):
            return str(self.date) 
        
        def month_totals(self):
            totalcheck = self.fifththird_check + self.huntington_check
            totalsave = self.fifththird_save + self.huntington_save \
                + self.capone_save + self.amex_save
            totalinvest = self.buckeye_invest + self.deacon_invest
            totalretire = self.opers_retire + self.four01_retire \
                + self.four57_retire + self.roth_retire
            totalphysical = self.justin_car+self.kat_car+self.main_home
            totalassets = totalcheck+totalsave+totalinvest+totalretire\
                +totalphysical
            totalcredit = self.amex_credit+self.discover_credit+self.capone_credit
            totalloan = self.car_loan+self.privstudent_loan+self.pubstudent_loan
            totalmortgage = self.main_mortgage
            totalliabilities = totalcredit+totalloan+totalmortgage
            networth = totalassets-totalliabilities
            return (totalcheck, totalsave, totalinvest, \
                    totalretire, totalphysical, totalassets, \
                    totalcredit, totalloan, totalmortgage, totalliabilities, \
                    networth) 

