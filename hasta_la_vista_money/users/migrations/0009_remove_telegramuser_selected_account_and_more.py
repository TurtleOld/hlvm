# Generated by Django 4.2.11 on 2024-04-11 21:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0008_remove_user_policy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='selected_account',
        ),
        migrations.RemoveField(
            model_name='telegramuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='SelectedAccount',
        ),
        migrations.DeleteModel(
            name='TelegramUser',
        ),
    ]
