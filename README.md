# Educa — образовательная платформа на Django

Educa — веб‑платформа для онлайн‑обучения на **Django** с модульными курсами и несколькими типами контента. Проект включает WebSocket‑чат на **Django Channels**, API на **Django REST Framework**, кэш/брокер на **Redis** и конфигурацию для запуска в **Docker** (PostgreSQL + Redis + Nginx + Daphne).

## Возможности

### Для преподавателей
- Создание и управление курсами
- Модульная структура курсов
- Добавление контента разных типов: текст, видео, изображения, файлы
- Управление порядком модулей и материалов
- Разграничение доступа к своим курсам

### Для студентов
- Просмотр доступных курсов
- Запись на курс (enrollment)
- Последовательное прохождение модулей

### Дополнительно
- Чат/комнаты в реальном времени (Channels)
- REST API для курсов
- Redis‑кэширование
- Management command для напоминаний о записи: `students/management/commands/enroll_reminder.py`

## Стек
- Python 3.12
- Django (в проекте указан Django 5.x)
- PostgreSQL
- Redis
- Django Channels + Daphne
- Django REST Framework
- Nginx (в docker‑окружении)

## Структура проекта (кратко)
- `educa/` — Django‑проект (settings/asgi/urls)
- `courses/` — курсы, модули, контент, шаблоны
- `students/` — логика студентов и записи на курсы
- `chat/` — WebSocket‑чат (consumers/routing/templates)
- `config/` — конфиги для nginx/uwsgi
- `docker-compose.yml`, `Dockerfile` — контейнеризация

## Быстрый старт (Docker)

Требования: установленный **Docker** и **Docker Compose**.

1) Собрать и запустить сервисы:
```bash
docker compose up --build
```

2) Применить миграции (в отдельном окне терминала):
```bash
docker compose exec web python manage.py migrate
```

3) Создать Суперпользователя:
```bash
docker compose exec web python manage.py createsuperuser
```

4) Открыть в браузере:
- Приложение: http://localhost/
- Админка: http://localhost/admin/

Примечание: в `docker-compose.yml` определены сервисы `web` и `daphne`. Для локального старта достаточно одного из них; в текущей конфигурации `web` уже запускает Daphne на 8000.

## Локальный запуск (без Docker)

Требования: Python 3.12, PostgreSQL и Redis (или измените настройки под SQLite).

1) Установить зависимости:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2) Настроить переменные окружения/настройки.

В проекте есть разные модули настроек:
- `educa/settings/local.py`
- `educa/settings/prod.py`
- `educa/settings/base.py`

Для запуска укажите нужный модуль:
```bash
set DJANGO_SETTINGS_MODULE=educa.settings.local
python educa/manage.py migrate
python educa/manage.py runserver
```

Для WebSocket/Channels в локальном окружении понадобится Redis и запуск через ASGI (например, daphne/uvicorn).

## Переменные окружения (Docker)

В `docker-compose.yml` передаются значения для подключения к Postgres:
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`

Также задаётся:
- `DJANGO_SETTINGS_MODULE=educa.settings.prod`

## Полезные команды

- Миграции:
```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

- Сбор статики (актуально для прод‑окружения):
```bash
docker compose exec web python manage.py collectstatic --noinput
```

- Напоминания о записи на курс (management command):
```bash
docker compose exec web python manage.py enroll_reminder
```

## Примечания по зависимостям

В репозитории присутствуют **два** файла `requirements.txt` (в корне и внутри `educa/`). Убедитесь, что используете тот, который соответствует вашему способу запуска.

Также обратите внимание: текущий `requirements.txt` в корне выглядит сохра��ённым в UTF‑16 (видны нулевые байты). Если при установке зависимостей `pip` ругается на формат файла, пересохраните его в UTF‑8.

## Лицензия

Не указана.
