from string import Template

from django import forms
from Main.models import Expense


class ExpenseCreateForm(forms.ModelForm):
    class Meta:

        model = Expense
        fields = ('name',)


class SearchForm(forms.Form):
    min_date = forms.DateField(label='Дата начала', required = False)
    max_date = forms.DateField(label='Дата окончания', required = False)