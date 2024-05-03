import telebot
import logging

# Настройка логгера
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = telebot.TeleBot('6878930455:AAEbqFls6xcLwbP47vAPiwl1JRYPgC1lvlw')

# Словарь с ссылками на ресурсы
resource_links = {
    "programming": {
        "Учебные ютуб-каналы": "",
        "Курсы": "ссылка_на_курсы_по_программированию",
        "Статьи": "ссылка_на_статьи_по_программированию"
    },
    "math": {
        "Учебные ютуб-каналы": "ссылка_на_каналы_по_математике",
        "Курсы": "ссылка_на_курсы_по_математике",
        "Статьи": "ссылка_на_статьи_по_математике"
    },
    "algebra": {
        "Учебные ютуб-каналы": "ссылка_на_каналы_по_алгебре",
        "Курсы": "ссылка_на_курсы_по_алгебре",
        "Статьи": "ссылка_на_статьи_по_алгебре"
    }
}

@bot.message_handler(commands=['start'])
def start(message):
    logger.info("start function called")
    bot.send_message(message.chat.id, "Привет! Я бот по подбору учебного материала! На какую тему ищите учебный материал?")
    bot.send_message(message.chat.id, "1. Программирование\n2. Математика\n3. Алгебра")

# Обработчики выбора тем и ресурсов
@bot.message_handler(func=lambda message: message.text == "1")
def programming_resources(message):
    logger.info("programming_resources function called")
    bot.send_message(message.chat.id, "Вот ресурсы по программированию:")
    for resource_type, link in resource_links["programming"].items():
        bot.send_message(message.chat.id, f"{resource_type}: {link}")

@bot.message_handler(func=lambda message: message.text == "2")
def math_resources(message):
    logger.info("math_resources function called")
    bot.send_message(message.chat.id, "Вот ресурсы по математике:")
    for resource_type, link in resource_links["math"].items():
        bot.send_message(message.chat.id, f"{resource_type}: {link}")

@bot.message_handler(func=lambda message: message.text == "3")
def algebra_resources(message):
    logger.info("algebra_resources function called")
    bot.send_message(message.chat.id, "Вот ресурсы по алгебре:")
    for resource_type, link in resource_links["algebra"].items():
        bot.send_message(message.chat.id, f"{resource_type}: {link}")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    logger.info("handle_text function called")
    text = message.text
    if text == "1":
        programming_resources(message)
    elif text == "2":
        math_resources(message)
    elif text == "3":
        algebra_resources(message)

# Запуск бота
bot.polling(none_stop=True)






