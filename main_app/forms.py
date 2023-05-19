from django import forms
from .models import Probleme, Solution



class ProblemeForm(forms.Form):
    nom = forms.CharField(label='Nom du problème', max_length=255)



class SolutionForm(forms.ModelForm):
    probleme = forms.ModelChoiceField(queryset=Probleme.objects.all().order_by('nom'))
    
    class Meta:
        model = Solution
        fields = ['probleme', 'description']
