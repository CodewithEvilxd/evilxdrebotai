import os
import telegram
import openai
from telegram.ext import Updater, MessageHandler, Filters

telegram_token = os.environ.get('5881385260:AAGbncp6c5f-RlbpzGe6F9GPCys9G4NTdPc')
openai_api_key = os.environ.get('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')

bot = telegram.Bot(token=telegram_token)
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

openai.api_key = openai_api_key
model_engine = "text-davinci-002"

def handle_message(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=100
    )
    bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
