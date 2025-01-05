from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

# Токен вашего бота
BOT_TOKEN = "7912823755:AAGEcJeF70J0B5L1fHuuiiGbz20rhVFQQuo"
CHAT_ID = "-1002333101731"  # ID чата или группы, куда отправлять сообщение
RULES_LINK = "https://telegra.ph/Pravila-gruppy-01-05-6"

bot = Bot(token=BOT_TOKEN)

def send_rules():
    message = f"Привет! Пожалуйста, ознакомьтесь с правилами нашей группы: {RULES_LINK}"
    bot.send_message(chat_id=CHAT_ID, text=message)

# Планировщик, чтобы отправлять сообщения каждый день
scheduler = BlockingScheduler()
scheduler.add_job(send_rules, 'interval', days=1)

if __name__ == "__main__":
    scheduler.start()