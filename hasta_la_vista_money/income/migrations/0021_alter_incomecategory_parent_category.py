# Generated by Django 4.2.9 on 2024-01-25 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('income', '0020_alter_incomecategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomecategory',
            name='parent_category',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='subcategories',
                to='income.incomecategory',
            ),
        ),
    ]
