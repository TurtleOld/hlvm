# Generated by Django 4.2.7 on 2023-11-05 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("income", "0009_alter_incometype_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incometype",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="category_income_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
