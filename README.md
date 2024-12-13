# Educational Modules API

API для управления образовательными модулями, созданный на Django и Django Rest Framework. Проект контейнеризирован с использованием Docker.

## Особенности

- Реализованы методы CRUD для модели "Образовательные модули".
- Автодокументация API с помощью Swagger и ReDoc.
- Контейнеризация с помощью Docker и Docker Compose.
- Поддержка PostgreSQL.

## Установка и запуск

### Требования

- Docker и Docker Compose должны быть установлены.
- Python 3.10 (если запускать локально, а не через Docker).

### Запуск с Docker

1. Клонируйте репозиторий:
   ```bash
   git clone <URL вашего репозитория>
   cd <имя папки репозитория>
   ```

2. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build
   ```

3. Примените миграции:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Откройте браузер и перейдите по адресу:
   - [http://127.0.0.1:8000/api/docs/swagger/](http://127.0.0.1:8000/api/docs/swagger/) — Swagger UI.
   - [http://127.0.0.1:8000/api/docs/redoc/](http://127.0.0.1:8000/api/docs/redoc/) — ReDoc.

### Запуск локально

1. Клонируйте репозиторий:
   ```bash
   git clone <URL вашего репозитория>
   cd <имя папки репозитория>
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Настройте базу данных PostgreSQL в `settings.py` и примените миграции:
   ```bash
   python manage.py migrate
   ```

4. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

5. Откройте браузер и перейдите по адресу [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

## Модель "Образовательные модули"

Модель имеет следующие поля:
- `order_number` — порядковый номер (целое число).
- `title` — название модуля (строка).
- `description` — описание модуля (текст).

## Эндпоинты

### Основные маршруты API:
- `GET /api/modules/` — получить список всех модулей.
- `POST /api/modules/` — создать новый модуль.
- `GET /api/modules/{id}/` — получить данные конкретного модуля.
- `PUT /api/modules/{id}/` — обновить модуль.
- `PATCH /api/modules/{id}/` — частично обновить модуль.
- `DELETE /api/modules/{id}/` — удалить модуль.

### Документация:
- Swagger UI: [http://127.0.0.1:8000/api/docs/swagger/](http://127.0.0.1:8000/api/docs/swagger/)
- ReDoc: [http://127.0.0.1:8000/api/docs/redoc/](http://127.0.0.1:8000/api/docs/redoc/)

## Тестирование

1. Запустите тесты:
   ```bash
   docker-compose exec web python manage.py test
   ```

2. Все модели, сериализаторы и представления покрыты тестами.

## Автор

- Жиров Даниил
- Email: danieelpark@gmail.com
- GitHub: https://github.com/DanielPyth1/

