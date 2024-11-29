import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import subprocess

# Включите логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Пароль для аутентификации
AUTH_PASSWORD = "rsgk"

# Словарь для хранения состояния аутентификации пользователей
authenticated_users = {}

# Определите функцию для обработки команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Используйте команду /login password для входа.')

# Определите функцию для обработки команды /login
async def login(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if len(context.args) != 1:
        await update.message.reply_text('Используйте команду /login password для входа.')
        return

    password = context.args[0]
    if password == AUTH_PASSWORD:
        authenticated_users[user_id] = True
        await update.message.reply_text('Аутентификация успешна. Теперь вы можете отправлять команды Linux.')
    else:
        await update.message.reply_text('Неверный пароль. Попробуйте снова.')

# Определите функцию для обработки текстовых сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if not authenticated_users.get(user_id):
        await update.message.reply_text('Вы не аутентифицированы. Используйте команду /login password для входа.')
        return

    user_message = update.message.text
    try:
        # Выполните команду Linux
        result = subprocess.run(user_message, shell=True, capture_output=True, text=True)
        # Отправьте результат обратно пользователю
        await update.message.reply_text(f'Результат:\n{result.stdout}\nОшибки:\n{result.stderr}')
    except Exception as e:
        await update.message.reply_text(f'Произошла ошибка: {str(e)}')

def main() -> None:
    # Вставьте сюда ваш токен API
    token = "7551211221:AAEC3csRZVJjyHwIcDraFAKwAaWlPZedo80"

    # Создайте приложение
    application = ApplicationBuilder().token(token).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик команды /login
    application.add_handler(CommandHandler("login", login))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запустите бота
    application.run_polling()

if __name__ == '__main__':
    main()
