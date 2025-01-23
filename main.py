import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Начальные параметры генерации пароля
user_settings = {
    # Количество слов
    "word_count": 4,  
    # Префиксы и суффиксы
    "include_prefix_suffix": True,  
    # Использовать спецсимволы и цифры в качестве разделителей
    "use_special_delimiters": False,  
}

# Список слов для генерации
WORDS = [
    "alpha","beta","gamma","delta","macho","omega","honey","unmovable","secure","encrust","random","entropy",
    "complex","quantum","vector","cipher","decode","matrix","galaxy","nebula","crystal","synergy",
    "fusion","pioneer","cosmos","vortex","horizon","spectrum","binary","infinity","gravity","orbit",
    "stellar","cluster","plasma","astral","cipher","guardian","lumen","comet","nova","phoenix",
    "zenith","pulse","pyro","ember","prism","obsidian","kepler","solaris","andromeda","nebular"
]

# Полный список символов
SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"

# Функция для генерации пароля
def generate_password(settings):
    word_count = settings["word_count"]
    include_prefix_suffix = settings["include_prefix_suffix"]
    use_special_delimiters = settings["use_special_delimiters"]

    # Генерация слов
    words = random.sample(WORDS, word_count)

    # Генерация разделителей
    if use_special_delimiters:
        delimiters = [random.choice(SYMBOLS) for _ in range(word_count - 1)]
    else:
        delimiters = [""] * (word_count - 1)

    # Генерация префиксов и суффиксов
    if include_prefix_suffix:
        words = [
            f"{random.choice(SYMBOLS)}{word}{random.choice(SYMBOLS)}"
            for word in words
        ]

    # Объединение слов с разделителями
    password = "".join(
        word + (delimiters[i] if i < len(delimiters) else "")
        for i, word in enumerate(words)
    )
    return password

# Функция для отображения настроек
def get_settings_markup():
    buttons = [
        [
            InlineKeyboardButton(
                f"Количество слов: {user_settings['word_count']}",
                callback_data="adjust_word_count",
            )
        ],
        [
            InlineKeyboardButton(
                f"Префиксы и суффиксы: {'Вкл' if user_settings['include_prefix_suffix'] else 'Выкл'}",
                callback_data="toggle_prefix_suffix",
            )
        ],
        [
            InlineKeyboardButton(
                f"Спецсимволы/разделители: {'Вкл' if user_settings['use_special_delimiters'] else 'Выкл'}",
                callback_data="toggle_special_delimiters",
            )
        ],
        [InlineKeyboardButton("Сгенерировать пароль", callback_data="generate_password")],
    ]
    return InlineKeyboardMarkup(buttons)

# Обработчик команды /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот для генерации сложных паролей. Выберите параметры генерации или нажмите 'Сгенерировать пароль':",
        reply_markup=get_settings_markup(),
    )

# Обработчик кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "adjust_word_count":
        # Увеличение количества слов в пароле (цикл от 2 до 8)
        user_settings["word_count"] = (
            user_settings["word_count"] + 1 if user_settings["word_count"] < 8 else 2
        )

    elif query.data == "toggle_prefix_suffix":
        # Переключение настройки префиксов и суффиксов
        user_settings["include_prefix_suffix"] = not user_settings["include_prefix_suffix"]

    elif query.data == "toggle_special_delimiters":
        # Переключение настройки разделителей
        user_settings["use_special_delimiters"] = not user_settings["use_special_delimiters"]

    elif query.data == "generate_password":
        # Генерация пароля
        password = generate_password(user_settings)
        await query.edit_message_text(
            f"Ваш сгенерированный пароль: `{password}`\n\nВы можете настроить параметры и сгенерировать новый пароль:",
            reply_markup=get_settings_markup(),
            parse_mode="Markdown",
        )
        return

    # Обновление сообщения с настройками
    await query.edit_message_text(
        "Обновлённые настройки генерации пароля:",
        reply_markup=get_settings_markup(),
    )

# Главная функция
def main():
    application = ApplicationBuilder().token("Ваш токен").build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()

if __name__ == "__main__":
    main()
