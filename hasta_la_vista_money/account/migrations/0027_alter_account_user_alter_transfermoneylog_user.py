# Generated by Django 4.2.11 on 2024-04-08 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            'account',
            '0026_rename_account_acc_name_ac_e74e62_idx_account_name_ac_dad2cb_idx_and_more',
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='account_users',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='transfermoneylog',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='transfer_money',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
