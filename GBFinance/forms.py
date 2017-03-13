from django import forms
from .models import MonthBal

class MonthBalForm(forms.ModelForm):
    
    class Meta:
        model = MonthBal
        fields = ('date', 'huntington_check', 'fifththird_check',  'huntington_save', 
                  'fifththird_save', 'capone_save', 'amex_save', 'deacon_invest',
                  'buckeye_invest', 'opers_retire', 'four57_retire', 'four01_retire', 'roth_retire',
                  'main_home', 'justin_car', 'kat_car', 'capone_credit', 'amex_credit', 
                  'discover_credit', 'car_loan', 'pubstudent_loan', 'privstudent_loan', 
                  'main_mortgage',)