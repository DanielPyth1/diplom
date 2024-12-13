# Базовый образ для Python
FROM python:3.10-slim

# Установим рабочую директорию
WORKDIR /app

# Скопируем файлы проекта
COPY . /app

# Установим зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Установим переменные окружения для Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Открываем порт
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
