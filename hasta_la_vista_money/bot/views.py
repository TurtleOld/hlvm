from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hasta_la_vista_money.bot.config_bot import bot_admin, bot_type
from hasta_la_vista_money.bot.receipt_parser_json import handle_receipt_json
from hasta_la_vista_money.bot.receipt_parser_text import handle_receipt_text


def webhooks(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf8')
        update = bot_type.Update.de_json(json_data)
        bot_admin.process_new_updates([update])
        return HttpResponse('Webhook processed successfully')
