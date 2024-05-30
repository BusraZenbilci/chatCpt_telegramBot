import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# OpenAI API anahtarınızı burada ayarlayın
openai.api_key = 'YOUR OPENAI KEY'

# Telegram Bot tokenınızı burada ayarlayın
TELEGRAM_TOKEN = 'YOUR TELEGRAM KEY'

def gpt35_chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Merhaba! Ben bir chatbotum. Bana sorularınızı sorabilirsiniz.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    response = gpt35_chatbot(user_input)
    await update.message.reply_text(response)

def main():
    # Application'ı bot tokenı ile oluşturun
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Dispatcher'da yeni bir komut işleyici ve mesaj işleyici ekleyin
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botu başlatın
    application.run_polling()

if __name__ == '__main__':
    main()
