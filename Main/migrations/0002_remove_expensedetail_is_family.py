# Generated by Django 2.0.7 on 2018-07-11 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensedetail',
            name='is_family',
        ),
    ]
