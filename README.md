# Cryptocurrency Price Parser

## Описание проекта
Этот проект представляет собой автоматизированный парсер цен криптовалют с сайта CoinMarketCap, созданный на Python с использованием библиотеки Playwright. Он позволяет регулярно собирать информацию о ключевых показателях криптовалют и отправлять уведомления о них в Telegram-бот. Система собирает данные каждые три часа и отправляет обновления с подробным отчетом по первым 10 криптовалютам по объёму торгов.

## Цели проекта
- Автоматизировать сбор данных с CoinMarketCap.
- Предоставлять регулярные отчёты о состоянии криптовалют в Telegram.
- Обеспечить удобные команды для получения данных в любой момент.

## Основные функции

### Сбор данных
- Сценарий автоматически собирает данные о первых 10 криптовалютах по объёму торгов.
- Для каждой криптовалюты собирается информация о текущей цене, процентном изменении за последние 24 часа и объёме торгов.
- Данные обновляются каждые 3 часа, с записью времени последнего обновления в JSON-файл.
- Обработка возможных ошибок при запросе, включая недоступность сайта, с функцией повторных попыток.

### Использование Playwright
- Для автоматизации работы с браузером используется Playwright в безголовом режиме (headless).
- Скрипт взаимодействует с CoinMarketCap, извлекая актуальные данные с минимальной задержкой.

### Telegram-бот
- Бот, созданный с помощью библиотеки `aiogram`, отправляет обновления пользователю после каждого успешного сбора данных.
- Поддерживаются команды:
  - `/start` — меню для управления.
  - `/logs` — отображает последние собранные данные о топ-10 криптовалютах.
  - `/currency <название>` — выдаёт данные по конкретной криптовалюте (например, `/currency Bitcoin`).

### Хранение данных
- Данные о ценах криптовалют сохраняются в JSON-файл с указанием времени последнего обновления.
- Telegram-бот отправляет пользователю только самые актуальные данные.

## Используемые технологии и библиотеки
- **[Playwright](https://playwright.dev/)** — автоматизация браузера для сбора данных.
- **[aiogram](https://docs.aiogram.dev/en/latest/)** — создание и управление Telegram-ботом.
- **[APScheduler](https://apscheduler.readthedocs.io/en/latest/)** — автоматическое планирование обновлений данных.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** и **[aiosqlite](https://github.com/omnilib/aiosqlite)** — для работы с базой данных.
- **[Loguru](https://loguru.readthedocs.io/)** — логирование событий.
- **[greenlet](https://greenlet.readthedocs.io/)** — поддержка асинхронности.

## Установка и запуск

### Шаг 1: Клонируйте репозиторий
```bash
git clone https://github.com/0x1eviathan/coinmarketcapparser.git
cd coinmarketcapparser
```

### Шаг 2: Создайте виртуальное окружение и установите зависимости
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
venv\Scripts\activate     # для Windows

pip install -r requirements.txt
```

### Шаг 3: Запустите проект
```bash
python -m src
```
