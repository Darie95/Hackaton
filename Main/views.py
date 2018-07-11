from django.shortcuts import render
from Main.forms import ExpenseCreateForm
from Main.models import Expense, ExpenseDetail
from django.views.generic import CreateView


def expense(request):
    exp = Expense.objects.all()
    return render(request, 'index.html', {'exp': exp})


class AddExpense(CreateView):
    template_name = 'create_expense.html'
    success_url = '/'
    model = Expense
    form_class = ExpenseCreateForm

    def get_context_data(self, **kwargs):
        context = super(AddExpense, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        model = form.save(commit=False)
        return super(AddExpense, self).form_valid(form)


def person(request, person_id):
    context = {'persons': ExpenseDetail.objects.filter(id=person_id).all()}
    return render(request, 'about_persons.html', context)
