# FreeHunter

Профессиональный Telegram-бот на Python для автоматического сбора полезной информации.

## Технологии

- Python 3.12+
- aiogram 3
- SQLite
- APScheduler
- aiohttp
- BeautifulSoup4
- lxml
- python-dotenv
- loguru

## Структура проекта

```
FreeHunter/
├── bot.py
├── config.py
├── database.py
├── scheduler.py
├── handlers/
├── services/
├── parsers/
├── keyboards/
├── utils/
└── data/
```

## Запуск

1. Создать виртуальное окружение.
2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Создать `.env` на основе `.env.example`.
4. Запустить:

```bash
python bot.py
```

## Статус разработки

Проект находится в активной разработке.
