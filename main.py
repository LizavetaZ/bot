from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import*




app = ApplicationBuilder().token("5873069701:AAHypQc7tY8K5--o6yHe3BddYs5FsZdeyhI").build()

app.add_handler(CommandHandler("hello", hi_command))
print('server start')
app.run_polling()