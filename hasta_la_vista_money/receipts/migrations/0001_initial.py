# Generated by Django 4.2.2 on 2023-06-26 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_seller', models.CharField(max_length=255)),
                ('retail_place_address', models.CharField(default='Нет данных', max_length=1000, null=True)),
                ('retail_place', models.CharField(blank=True, default='Нет данных', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Нет данных', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('nds_type', models.IntegerField(blank=True, default=None, null=True)),
                ('nds_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField()),
                ('number_receipt', models.IntegerField(default=None, null=True)),
                ('operation_type', models.IntegerField(blank=True, choices=[(1, 'Приход'), (2, 'Возврат прихода'), (3, 'Расход'), (4, 'Возврат расхода')], default=0, null=True)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.account')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='receipts.customer', verbose_name='customer')),
                ('product', models.ManyToManyField(related_name='product', to='receipts.product')),
            ],
        ),
    ]
