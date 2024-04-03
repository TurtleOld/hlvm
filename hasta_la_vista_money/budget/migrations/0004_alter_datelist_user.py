# Generated by Django 4.2.10 on 2024-04-03 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("budget", "0003_alter_planning_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datelist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="budget_date_list_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
