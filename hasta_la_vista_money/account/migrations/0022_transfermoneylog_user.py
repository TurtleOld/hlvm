# Generated by Django 4.2.10 on 2024-03-18 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0021_remove_transfermoneylog_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="transfermoneylog",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfer_money",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
