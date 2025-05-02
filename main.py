from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# BOT_TOKEN = '8122325803:AAHpLQ0uR5H4pQm8WHiEZoUysDThogv1PeU'
# OWNER_CHAT_ID =1377944646
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_CHAT_ID = int(os.getenv("OWNER_CHAT_ID"))


async def forward_to_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    await context.bot.send_message(
        chat_id=OWNER_CHAT_ID,
        text=f"📩 New message from {user.first_name} (@{user.username}):\n\n{text}"
    )


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_owner))
app.run_polling()
