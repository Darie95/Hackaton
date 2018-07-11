from django.shortcuts import render

from Main.models import Expense


def expense(request):
    exp = Expense.objects.all()
    return render(request, 'index.html', {'exp': exp})
