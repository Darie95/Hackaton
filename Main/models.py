from django.db import models


class Expense (models.Model):
    class Meta:
        verbose_name = "Расходы"
        verbose_name_plural = "Расходы"

    def __str__(self):
        return '[{}| Expense {}]'.format(self.id, self.name)

    name = models.CharField(max_length=250, verbose_name="Статья расходов")


class Person (models.Model):
    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return '[{}| Expense {}]'.format(self.id, self.name)

    name = models.CharField(max_length=250, verbose_name="Имя человека")



class ExpenseDetail (models.Model):
    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"

    def __str__(self):
        return '[{}| ExpenseDetail {}]'.format(self.id, self.description)

    description = models.TextField(verbose_name="Описание расходов")
    amount = models.IntegerField(verbose_name="Сумма расходов")
    date = models.DateField(verbose_name="Дата расхода")

    person = models.ForeignKey(Person, related_name='exp_details',
                                on_delete=models.CASCADE, verbose_name="Люди")

    expense = models.ForeignKey(Expense, related_name='expenses',
                             on_delete=models.CASCADE, verbose_name="Категория")


class Income(models.Model):
    class Meta:
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"

    def __str__(self):
        return '[{}| ExpenseDetail {}]'.format(self.id, self.name)

    name = models.CharField(max_length=250)
    amount = models.IntegerField(verbose_name="Сумма расходов")
    date = models.DateField(verbose_name="Дата расхода")
    person = models.ForeignKey(Person, related_name='people',
                               on_delete=models.CASCADE, verbose_name="Люди")





