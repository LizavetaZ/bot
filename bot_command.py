from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')