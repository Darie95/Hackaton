from string import Template

from django import forms
from Main.models import Expense


class ExpenseCreateForm(forms.ModelForm):
    class Meta:

        model = Expense
        fields = ('name',)
