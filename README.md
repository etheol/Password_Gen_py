## 🔐 Telegram Password Generator Bot

> Бот, который создаёт **запоминающиеся, но сложные пароли** — прямо в Telegram.  
> Настраиваемый, интерактивный, без лишних зависимостей.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-2CA5E0?logo=telegram&style=flat-square)](https://core.telegram.org/bots)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

---

### 🌟 Особенности

- ✅ Генерация паролей из **человеко-читаемых слов** (например: `@alpha#gamma~delta!`)
- ⚙️ **Полная настройка в интерфейсе**: количество слов, префиксы/суффиксы, разделители
- 🎯 **Inline-кнопки** — удобное управление без лишних команд
- 📋 Пароли выводятся в формате `кода` — легко копировать
- 🚀 Запускается за 2 минуты — нужен только Python и токен от [@BotFather](https://t.me/BotFather)

---

### 🛠️ Технологии

```python
python-telegram-bot  # Официальная библиотека Telegram Bot API
logging              # Для отслеживания работы бота
random               # Генерация случайных комбинаций
