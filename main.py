from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! I'm your friendly bot. How can I assist you today?"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Get help with commands\n"
        "/about - Learn more about this bot"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "This bot is designed to assist you with various tasks. "
        "Feel free to ask me anything!" 
        "Created by Muratbekov Sultanbek."
    )

app = ApplicationBuilder().token("7613016699:AAF7hv7IC-KavkCQQ9aGKlzFHnz69kEtqSw").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))

print("Bot is polling...")
app.run_polling()