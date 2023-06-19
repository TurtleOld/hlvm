# Generated by Django 4.2.2 on 2023-06-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_expensetype_alter_expense_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
