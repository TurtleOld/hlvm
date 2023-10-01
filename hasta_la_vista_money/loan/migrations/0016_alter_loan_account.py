# Generated by Django 4.2.5 on 2023-10-01 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0009_account_account_acc_name_ac_e74e62_idx"),
        ("loan", "0015_alter_loan_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="account.account",
            ),
        ),
    ]
