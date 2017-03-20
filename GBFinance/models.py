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
        
        def total_check(self):
            totalcheck = self.fifththird_check + self.huntington_check
            return totalcheck
        
        def total_save(self):
            totalsave = self.fifththird_save + self.huntington_save \
                + self.capone_save + self.amex_save
            return totalsave
        
        def total_invest(self):
            totalinvest = self.buckeye_invest + self.deacon_invest
            return totalinvest
        
        def total_retire(self):
            totalretire = self.opers_retire + self.four01_retire \
                + self.four57_retire + self.roth_retire
            return totalretire
        
        def total_physical(self):
            totalphysical = self.justin_car+self.kat_car+self.main_home
            return totalphysical
        
        def total_assets(self):
            totalassets = self.fifththird_check + self.huntington_check + \
                self.fifththird_save + self.huntington_save \
                + self.capone_save + self.amex_save + \
                self.buckeye_invest + self.deacon_invest + \
                self.opers_retire + self.four01_retire \
                + self.four57_retire + self.roth_retire + \
                self.justin_car+self.kat_car+self.main_home
            return totalassets
            
        def total_credit(self):
            totalcredit = self.amex_credit+self.discover_credit+self.capone_credit
            return totalcredit
        
        def total_loan(self): 
            totalloan = self.car_loan+self.privstudent_loan+self.pubstudent_loan
            return totalloan 
            
        def total_mortgage(self):
            totalmortgage = self.main_mortgage
            return totalmortgage
        
        def total_liabilities(self):
            totalliabilities = self.amex_credit+self.discover_credit + \
            self.capone_credit + self.car_loan+self.privstudent_loan + \
            self.pubstudent_loan + self.main_mortgage
            return totalliabilities
            
        def networth(self):
            assets = self.total_assets()
            liabilities = self.total_liabilities()
            networth = assets - liabilities
            return networth 

            
class MonthInc(models.Model):
    date = models.DateField()
    huntington_interest = models.DecimalField(max_digits=8, decimal_places=2)
    fifththird_interest = models.DecimalField(max_digits=8, decimal_places=2)
    capone_interest = models.DecimalField(max_digits=8, decimal_places=2)
    amex_interest = models.DecimalField(max_digits=8, decimal_places=2)
    schwab_interest = models.DecimalField(max_digits=8, decimal_places=2)
    schwab_dividends = models.DecimalField(max_digits=8, decimal_places=2)
    expense_checks = models.DecimalField(max_digits=8, decimal_places=2)
    miscellaneous_income = models.DecimalField(max_digits=8, decimal_places=2)
    refund_rebate_repayment = models.DecimalField(max_digits=8, decimal_places=2)
    gift_income = models.DecimalField(max_digits=8, decimal_places=2)
    supremecourt_salary = models.DecimalField(max_digits=8, decimal_places=2)
    cdm_salary = models.DecimalField(max_digits=8, decimal_places=2)
    opers_retirement = models.DecimalField(max_digits=8, decimal_places=2)
    four57b_retirement = models.DecimalField(max_digits=8, decimal_places=2)
    four01k_retirement = models.DecimalField(max_digits=8, decimal_places=2)
    roth_retirement = models.DecimalField(max_digits=8, decimal_places=2)
    schwab_investments = models.DecimalField(max_digits=8, decimal_places=2)
    amex_savings = models.DecimalField(max_digits=8, decimal_places=2)
    fifththird_savings = models.DecimalField(max_digits=8, decimal_places=2)
    capone_savings = models.DecimalField(max_digits=8, decimal_places=2)
    five29_college = models.DecimalField(max_digits=8, decimal_places=2)
    huntington_savings = models.DecimalField(max_digits=8, decimal_places=2)
    federal_tax = models.DecimalField(max_digits=8, decimal_places=2)
    social_security = models.DecimalField(max_digits=8, decimal_places=2)
    medicare = models.DecimalField(max_digits=8, decimal_places=2)
    ohio_tax = models.DecimalField(max_digits=8, decimal_places=2)
    columbus_tax = models.DecimalField(max_digits=8, decimal_places=2)
    health_insurance = models.DecimalField(max_digits=8, decimal_places=2)
    supplementallife_insurance = models.DecimalField(max_digits=8, decimal_places=2)
    flex_spending = models.DecimalField(max_digits=8, decimal_places=2)
    cdm_std = models.DecimalField(max_digits=8, decimal_places=2)
    cdmsupplemental_ltd = models.DecimalField(max_digits=8, decimal_places=2)
    parking = models.DecimalField(max_digits=8, decimal_places=2)
    parking_admin = models.DecimalField(max_digits=8, decimal_places=2)
    main_mortgage = models.DecimalField(max_digits=8, decimal_places=2)
    hoa_fees = models.DecimalField(max_digits=8, decimal_places=2)
    auto_insurance = models.DecimalField(max_digits=8, decimal_places=2)
    aep_electric = models.DecimalField(max_digits=8, decimal_places=2)
    rumpke_trash = models.DecimalField(max_digits=8, decimal_places=2)
    delaware_sewer = models.DecimalField(max_digits=8, decimal_places=2)
    delco_water = models.DecimalField(max_digits=8, decimal_places=2)
    suburban_gas = models.DecimalField(max_digits=8, decimal_places=2)
    verizon_kat = models.DecimalField(max_digits=8, decimal_places=2)
    sprint_justin = models.DecimalField(max_digits=8, decimal_places=2)
    directtv_cable = models.DecimalField(max_digits=8, decimal_places=2)
    timewarner_internet = models.DecimalField(max_digits=8, decimal_places=2)
    caponeauto_loan = models.DecimalField(max_digits=8, decimal_places=2)
    public_loan = models.DecimalField(max_digits=8, decimal_places=2)
    private_loan = models.DecimalField(max_digits=8, decimal_places=2)
    capone_creditcard = models.DecimalField(max_digits=8, decimal_places=2)
    amex_creditcard = models.DecimalField(max_digits=8, decimal_places=2)
    discover_creditcard = models.DecimalField(max_digits=8, decimal_places=2)
    kohls_vicsec_macy_eddiebauer_creditcards = models.DecimalField(max_digits=8, decimal_places=2)
    katwork_creditcard = models.DecimalField(max_digits=8, decimal_places=2)
    cashorcheck_purchases = models.DecimalField(max_digits=8, decimal_places=2)
    daycare = models.DecimalField(max_digits=8, decimal_places=2)
    taxdeductible_giving = models.DecimalField(max_digits=8, decimal_places=2)
    
    
    

