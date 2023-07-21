# MicroserviceTestProject
 
это микросервис, реализованный на языке программирования Python с использованием Django и Django REST framework. Микросервис предоставляет API для управления задачами и пользовательскими аккаунтами.

Требования
Перед запуском микросервиса убедитесь, что у вас установлены следующие компоненты:

Python (рекомендуется версия 3.7 и выше)
Docker и Docker Compose (для развертывания БД и контейнеров)
Установка
Склонируйте репозиторий MicroserviceTestProject на свой компьютер:
```
git clone https://github.com/your-username/MicroserviceTestProject.git
cd MicroserviceTestProject
```
Установите зависимости:
```
pip install -r requirements.txt
```

Запустите микросервис и базу данных с помощью Docker Compose
```
docker-compose up -d
```

Микросервис будет доступен по адресу http://localhost:8000/

API Endpoints:

Регистрация пользователей: POST /api/register/

Аутентификация пользователей: POST /api/login/

Получение списка пользователей: GET /api/users/

Тестирование
Для запуска тестов, выполните следующую команду:
```
pytest
```
