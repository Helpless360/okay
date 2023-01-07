import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

openai.api_key = "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"

def start(update, context):
    update.message.reply_text("Hi there! I'm a GPT chatbot. Ask me anything and I'll try my best to respond.")

def chat(update, context):
    message = update.message.text
    response = openai.Completion.create(engine="text-davinci-002", prompt=message, max_tokens=1024).get("choices")[0].get("text")
    update.message.reply_text(response)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("5902218782:AAGuN3K_re2XoGknwdIWPlWU0ZvwkPciFz4", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, chat))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
