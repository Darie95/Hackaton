from django.contrib import admin

# Register your models here.
from Main.models import ExpenseDetail, Income

admin.site.register(ExpenseDetail)
admin.site.register(Income)
