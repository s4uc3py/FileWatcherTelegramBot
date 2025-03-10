# 🤖 Telegram Folder Monitor Bot

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-red)](https://core.telegram.org/bots)

Бот для мониторинга файловых изменений в реальном времени с уведомлениями в Telegram.

---

## 🚀 Особенности
✅ **Мгновенные оповещения** о создании/изменении файлов  
✅ **Анти-спам** с задержкой 2 секунды  
✅ Поддержка **вложенных папок** (рекурсивный мониторинг)  
✅ Простая настройка через конфигурационные переменные  
✅ Работает на Windows, Linux и macOS

---

## 📝 Требования
- Python 3.8+
- Библиотеки: `watchdog`, `requests`

Установите зависимости:
```bash
pip install -r requirements.txt
```

## 🛠 Настройка
Создайте бота в Telegram
Начните чат с @BotFather
Используйте /newbot для создания
Скопируйте API Token (пример: 123456:ABC-DEF1234...)
Получите Chat ID
Напишите сообщение вашему боту
Откройте https://api.telegram.org/bot<ВАШ_ТОКЕН>/getUpdates
Найдите "id": 123456789 в ответе
Настройте конфигурацию
В файле main.py укажите:
```bash
TELEGRAM_TOKEN = 'ваш_токен_от_бота'  # Пример: '123456:ABC-DEF1234...'
CHAT_ID = 'ваш_chat_id'               # Пример: '123456789'
WATCH_PATH = r'C:\Путь\К\Вашей\Папке'  # Используйте сырые строки для Windows\ Может быть и шара напривер: \\Test-fs-01\
```
##🎬 Использование
Запустите бота:
```bash
python main.py
```
Пример уведомления в Telegram:
```bash
✅ Новый файл создан: report_2024.pdf
🔄 Файл изменен: notes.txt
```

⚙️ Кастомизация
Измените время анти-спама:
```bash
DEBOUNCE_TIME = 5  # Задержка в секундах
```
Добавьте фильтры файлов:
```bash
# В функции handle_event
if not file_name.endswith('.tmp'):
    send_telegram_message(...)
```
## 🤝 Помощь проекту
Добавьте звезду ⭐️ в GitHub
Сообщайте о багах в Issues
Предлагайте улучшения в Pull Requests
