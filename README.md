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
### Авторы

**Супонин Кирилл**
