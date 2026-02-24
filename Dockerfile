# Взять официальный базовый образ Python платформы Docker
FROM python:3.12-slim-bookworm

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Задать рабочий каталог
WORKDIR /code/educa

# ⚠️ ЭТОТ БЛОК ОБЯЗАТЕЛЕН ДЛЯ СБОРКИ UWSGI, да и в целом геморой проще на Перейти на Daphne полностью
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     libjpeg-dev \
#     zlib1g-dev \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# Установить зависимости
RUN pip install --upgrade pip
COPY requirements.txt /code/educa/
RUN pip install -r requirements.txt

# Скопировать проект
COPY . /code/educa/

# Запуск через Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "educa.asgi:application"]