from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import json
import os
import random

TOKEN = "ВАШ_ТОКЕН_БОТА"
CHANNEL_ID = "@your_private_channel"  # ваш канал

USERS_FILE = "bot/users.json"

# Загружаем пользователей
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        users = json.load(f)
else:
    users = []

greetings = [
    "Привет. Добро пожаловать в систему обнаружения Васи.",
    "Привет. Этот бот иногда видит Васю там, где его нет.",
    "Добро пожаловать в детектор Васи.",
    "Кажется Вася где-то рядом…",
    "Система наблюдения за Васей почти активна."
]

def save_users():
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False)

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in users:
        update.message.reply_text("✅ Вы уже зарегистрированы и можете пользоваться ботом")
        return

    users.append(user_id)
    save_users()

    greeting = random.choice(greetings)
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Открыть радар", url="https://your-miniapp.vercel.app")]])
    update.message.reply_text(f"{greeting}\n\nПодпишись на канал и напиши /verefi", reply_markup=keyboard)

def verifi(update: Update, context: CallbackContext):
    # Простейшая заглушка проверки подписки
    update.message.reply_text("✅ Проверка подписки пройдена. Можете открывать Mini App!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verefi", verifi))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()