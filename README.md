## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

    ```sh
    git clone https://github.com/p1mcky/api_final.git
    cd api_final_yatube
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

