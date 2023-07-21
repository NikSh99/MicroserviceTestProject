# Dockerfile

# Базовый образ Python
FROM python:3.10

# Установка переменной окружения для запуска в режиме Production
ENV DJANGO_SETTINGS_MODULE=microservice_project.settings

# Установка зависимостей
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Копирование исходного кода
COPY microservice_project /app/

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
