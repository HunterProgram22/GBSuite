from django import forms
from .models import MonthBal

class MonthBalForm(forms.ModelForm):
    
    class Meta:
        model = MonthBal
        fields = ('date', 'fifththird_check', 'huntington_check', 'fifththird_save',
                  'huntington_save', 'capone_save', 'amex_save', 'buckeye_invest',
                  'deacon_invest', 'four57_retire', 'four01_retire', 'roth_retire',
                  'opers_retire', 'justin_car', 'kat_car', 'main_home', 'car_loan', 
                  'pubstudent_loan', 'privstudent_loan', 'main_mortgage', 'amex_credit', 
                  'discover_credit', 'capone_credit',)