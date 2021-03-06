from django import forms

from .models import Round, Course, Shots, PuttPractice, RangeDrill, ChipDrill


class RoundForm(forms.ModelForm):

    class Meta:
        model = Round
        fields = ('course', 'date', 'holesplayed', 'strokes', 'putts',
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


class PuttForm(forms.ModelForm):

    class Meta:
        model = PuttPractice
        fields = ('date', 'distance', 'attempts', 'makes')


class ChipForm(forms.ModelForm):

    class Meta:
        model = ChipDrill
        fields = ('date', 'drill', 'club', 'balls_hit', 'balls_ontarget')


class RangeForm(forms.ModelForm):

    class Meta:
        model = RangeDrill
        fields = ('date', 'drill', 'club', 'balls_hit')
