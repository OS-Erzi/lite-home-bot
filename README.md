<h1 align="center"><em>Lite Home Bot</em></h1>

<h3 align="center">
  Создавался для персонального использования
</h3>

<p align="center">
  <a href="https://www.python.org/downloads"><img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python"></a>
  <a href="https://github.com/Pycord-Development/pycord"><img src="https://img.shields.io/badge/pycord-2.6.1-blue.svg" alt="Python"></a>
  <a href="https://github.com/donBarbos/telegram-bot-template/blob/main/LICENSE"><img src="https://img.shields.io/github/license/OS-ERZI/lite-home-bot?color=blue" alt="License"></a>
<p>

## ✨ Features

-   [x] Верификация с выдачей роли
-   [x] Окно c информацией (роли/команды/каналы)
-   [x] Система анонимного чата (почему нет?)
-   [x] Выдача игровых ролей

## 🚀 Установка

#### Python 3.8 или новее

-   Для установки библиотеки рекомендуется использовать [виртуальную среду](https://docs.python.org/3/library/venv.html), особенно в Linux, где система Python управляется извне и ограничивает пакеты, которые вы можете на нее установить.

    ```bash
    python3 -m venv venv #Окружение
    
    pip install -r requirements.txt #установка библиотек
    ```

-   Настройте переменные среды в файле `.env`

-   Запуск

    ```bash
    python3 main.py
    ```

## 🌍 Переменные .env

| Название                 | Описание                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| `TOKEN`                  | Токен вашего дискорд бота                                                                   |
| `PREFIX`                 | Префикс бота                                                                                |
| `LOAD_TITLE`             | Консольная надпись загрузки                                                                 |
| `CUSTOM_COGS_FOLDER`     | Папка с винтами (cogs по стандарту)                                                         |
| `MAIN_COLOR`             | Цвет эмбедов                                                                                |
| `CROSS_EMOJI`            | Эмодзи крестика (для отрицательных действий)                                                |
| `CHECKMARK_EMOJI`        | Эмодзи галочки (для положительных действий)                                                 |
| `STARTMARK_EMOJI`        | Эмодзи звездочки или другой символ для начала                                               |
| `VERIFY_BANNER`          | Баннер для верификации                                                                      |
| `RULES_BANNER`           | Баннер для правил                                                                           |
| `COMMANDS_BANNER`        | Баннер для команд                                                                           |
| `NAVIGATION_BANNER`      | Баннер для навигации                                                                        |
| `TICKET_BANNER`          | Баннер для тикетов                                                                          |
| `INVISIBLE_BANNER`       | Невидимый баннер (может быть пустым изображением)                                           |
| `GAME_ROLES_BANNER`      | Баннер для игровых ролей                                                                    |
| `GUILD_ID`               | ID сервера                                                                                  |
| `OWNER_ID`               | ID владельца бота                                                                           |
| `VERIFY_CHANNEL_ID`      | ID канала верификации                                                                       |
| `RULES_CHANNEL_ID`       | ID канала с правилами                                                                       |
| `TICKET_CHANNEL_ID`      | ID канала для создания тикетов                                                              |
| `ROLES_CHANNEL_ID`       | ID канала с ролями                                                                          |
| `NAVIGATION_CHANNEL_ID`  | ID канала навигации                                                                         |
| `ANONIM_CHANNEL_ID`      | ID канала для анонимных сообщений                                                           |
| `ID_CATEGORY_FOR_TICKETS`| ID категории для тикетов                                                                    |
| `ANONIM_LOG_CHANNEL`     | ID канала для логов анонимных сообщений                                                     |
| `ALERT_ROLE_ID`          | ID роли для оповещений                                                                      |
| `RATE_ROLE_ID`           | ID роли для возрастного ограничения                                                         |

## 📂 Структура проекта

```bash
.
├── venv/#Виртуальное окружение
│
├── cogs # винты
│   ├── commands.py
│   └── events.py
│
├── core # ядро проекта
│   ├── __init__.py
│   ├── base.py #Класс запуска
│   ├── config.py #Подгрузка переменных
│   └── loader.py #Запуск бота
│
├── logger # Логирование
│   ├── logs/ #Сохранение логов бота
│   ├── tickets/ #Сохранинение билет обращения
│   ├── __init__.py
│   └── loguru_cfg.py #Конфиг логов
│
├── structs # Классы и функции для винтов
│   ├── __init__.py
│   ├── anonimus.py
│   ├── buttons.py
│   └── ticket.py 
│
├── .gitignore # Список игнора
├── .env # переменная среда
├── main.py # вход
├── LICENSE.md # Лицензия
└── README.md # Документация
```

## 🔧 Бибилиотеки

-   `pycord` — Библиотека для работы с discord API
-   `pydantic` — Библиотека для проверки данных
-   `loguru` — Библиотека для упрощения логирования

## 📝 Лицензия

Распространяется по лицензии MIT. См. [`LICENSE`](./LICENSE.md) для получения дополнительной информации.
