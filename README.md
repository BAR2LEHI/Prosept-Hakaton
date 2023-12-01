# project_backend
Backend для проекта хакатона "Яндекс.Практикум" и "ПРОСЕПТ"

## Авторы:
```
- Владислав Тарасов(https://github.com/BAR2LEHI)
- Анастасия Пушкарная(https://github.com/Anastasia7Si)
```

## Технологии:
```
- Python 3.11
- Fastapi 0.104
- Uvicorn 0.24
- SQLAlchemy 2.0
- Gunicorn 21.2
- Docker 6.1.3
```

## Реализовано: 
```
``` 

## В работе: 
```
```

## Запуск
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Anastasia7Si/project_backend.git
cd project_backend
```

### Для запуска контейнеров (доступ по http://localhost:80/)
```

```
- Создать файл .env и прописать в него свои данные.
Пример:
```
DB_NAME=db_name
DB_USER=db_user
DB_PASS=db_password
DB_HOST=db_host_name
DB_PORT=db_port
DATABASE_URL=db_url
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
POSTGRES_DB=db_name
POSTGRES_PORT=db_port
POSTGRES_SERVER=db_host_name
```
Запуск проекта
```
docker-compose up -d
```
Создание суперпользователя
```
```

### Для запуска проекта локально (доступ по http://127.0.0.1:8000/)
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить проект:
```
uvicorn src.main:app
```

## Запуск тестов
- 
```

```
## К проекту подключена документация, в которой можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```

```