from django.shortcuts import render
from Main.forms import ExpenseCreateForm, SearchForm
from Main.models import Expense, ExpenseDetail, Income, Person
from django.views.generic import CreateView, FormView
from django.db.models import Sum


def expense(request):
    # details = {
    #     person: [
    #         detail.expense for detail in person.exp_details.all()
    #     ] for person in Person.objects.all()
    # }
    person = Person.objects.all()
    return render(request, 'index.html', {'person': person})


def edit(request, expense_id):
    expense = ExpenseDetail.objects.filter(expense_id=expense_id).all()
    name = Expense.objects.filter(id = expense_id).first()
    return render(request, 'edit.html', {'expense': expense, 'name': name })


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
    a = ExpenseDetail.objects.filter(person=person_id).aggregate(Sum('amount'))
    b = ExpenseDetail.objects.filter(person=person_id).aggregate(Sum('amount'))
    c = int(b['amount__sum'])-int(a['amount__sum'])
    context = {'persons': ExpenseDetail.objects.filter(person=person_id).all(),
               'incomes': Income.objects.filter(person=person_id).all(),
               'names': Person.objects.filter(id=person_id).first(),
               'sum_exp': a,
               'sum_inc': b,
               'rest': c}
    return render(request, 'about_persons.html', context)


class Search(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def form_valid(self, form, person_id):
        data = form.cleaned_data
        result_exp = ExpenseDetail.objects.filter(person=person_id).all()
        result_inc = Income.objects.filter(person=person_id).all()
        if data['min_date']:
            result_exp = result_exp.filter(date__gte=data['min_date'])
        if data['max_date']:
            result_inc = result_inc.filter(price__lte=data['max_date'])
        a = result_exp.aggregate(Sum('amount'))
        b = result_inc.aggregate(Sum('amount'))
        c = int(b['amount__sum']) - int(a['amount__sum'])
        context = {'persons': result_exp,
                   'incomes': result_inc,
                   'names': Person.objects.filter(id=person_id).first(),
                   'sum_exp': a,
                   'sum_inc': b,
                   'rest': c}
        return render(self.request, 'about_persons.html', context)