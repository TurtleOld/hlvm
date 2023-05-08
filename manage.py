#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from hasta_la_vista_money.bot.config_bot import bot_admin


token_bot = os.environ.get('TOKEN_TELEGRAM_BOT')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'config.django.base')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    bot_admin.delete_webhook()
    bot_admin.set_webhook(f'https://money.pavlovteam.ru/bot/webhooks/')
    main()
