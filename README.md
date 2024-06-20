# Описание проекта api_final

Проект api_final представляет собой API для веб-приложения yatube. API разработан для обеспечения доступа к основным функциям приложения, таким как создание постов, комментариев, подписок на пользователей и других операций.

### Функции API

1. **Аутентификация**: Для доступа к API неаутентифицированным пользователям предоставляется только чтение данных, за исключением ресурса /follow/. Аутентифицированные пользователи имеют возможность изменять и удалять свои данные.
   
2. **Ресурсы**: API предоставляет доступ к следующим ресурсам:
   - Посты (/api/v1/posts/)
   - Комментарии (/api/v1/posts/{post_id}/comments/)
   - Подписки (/api/v1/follow/)
   - Группы (/api/v1/groups/)

### Технологии

- **Python 3.7**: Язык программирования, на котором написан проект.
- **Django 3.2.16**: Веб-фреймворк для быстрой разработки веб-приложений на Python.
- **Django Rest Framework 3.12.4**: Мощный и гибкий инструментарий для создания веб-API на основе Django.

### Установка и развертывание проекта

1. Клонировать репозиторий и перейти в него в командной строке:

    ```sh
    git clone https://github.com/p1mcky/api_final.git
    cd api_final
    ```

2. Создать и активировать виртуальное окружение:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Установить зависимости из файла `requirements.txt`:

    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Выполнить миграции:

    ```sh
    python3 manage.py migrate
    ```

5. Запустить проект:

    ```sh
    python3 manage.py runserver
    ```

### Документация к API

После запуска сервера документация к API доступна по адресу:
http://127.0.0.1:8000/redoc/

### Примеры запросов и ответов

#### Получение списка постов

**Запрос:**
```http
GET http://127.0.0.1:8000/api/v1/posts/
```

**Ответ:**
```json
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=3",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 1,
            "author": "string",
            "text": "string",
            "pub_date": "2024-01-06T10:01:17.379356Z",
            "image": "string",
            "group": 0
        },
        {
            "id": 2,
            "author": "string",
            "text": "string",
            "pub_date": "2024-01-06T10:42:39.054978Z",
            "image": "string",
            "group": 0
        }
    ]
}
```

#### Создание нового поста

**Запрос:**
```http
POST http://127.0.0.1:8000/api/v1/posts/
```

**Тело запроса:**
```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

**Ответ:**
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2024-01-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

#### Публикация и получение комментариев к постам

**Запрос:**
```http
GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

**Ответ:**
```json
[
    {
        "id": 1,
        "author": "string",
        "post": 1,
        "text": "string",
        "created": "2024-01-06T10:59:31.721673Z"
    }
]
```

**Запрос:**
```http
POST http://127.0.0.1:8000/api/v1/posts/1/comments/
```

**Тело запроса:**
```json
{
    "text": "1st comment"
}
```

**Ответ:**
```json
{
    "id": 1,
    "author": "string",
    "post": 1,
    "text": "string",
    "created": "2024-01-06T10:59:31.721673Z"
}
```

#### Подписка на авторов

**Запрос:**
```http
GET http://127.0.0.1:8000/api/v1/follow/
```

**Ответ:**
```json
[
    {
        "user": "string",
        "following": "string"
    }
]
```

**Запрос:**
```http
POST http://127.0.0.1:8000/api/v1/follow/
```

**Тело запроса:**
```json
{
    "following": "string"
}
```

**Ответ:**
```json
{
    "user": "string",
    "following": "string"
}
```

### Авторы

**Супонин Кирилл**
