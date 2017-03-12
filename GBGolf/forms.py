from django import forms

from .models import Round, Course, Shots

class RoundForm(forms.ModelForm):
    
    class Meta:
        model = Round
        fields = ('course', 'date', 'strokes', 'putts', 
                  'fairways_hit', 'gir', 'equistrokes')
        

class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ('course', 'rating', 'slope', 'par')
        
class ShotsForm(forms.ModelForm):
    
    class Meta:
        model = Shots
        fields = ('date', 'drdist', 'dracc', 'par3tee', 'lngdist', 'lngacc',
                  'shtdist', 'shtacc', 'pitch', 'chip', 'putt', 'penal',
                  'coursemgmt')
        