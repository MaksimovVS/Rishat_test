# Тестовые задания от Rishat_test

[Ссылка на сервер]() для ручного тестирования.

Необходимо клонировать репозиторий, создать и активировать виртуальное окружение и установить зависимости.

```bash
git clone git@github.com:MaksimovVS/Rishat_test.git

# windows
python -m venv venv
source venv/Scripts/activate 
# linux
python3 -m venv venv
source venv/bin/activate 

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполните миграции и запустите сервер:
```bash
cd rishat
python manage.py migrate
python manage.py runserver
```

Создайте суперпользователя
```bash
python manage.py createsuperuser
```

Доступные адреса:

Получения id сессии:
http://127.0.0.1:8000/buy/<pk>/
>>> {"id": "cs_test_a1NIGh48V4CVcIePpX5ycRen90uziAWJW7j7UvQY6xMqrN6JMnecy1YlBA"}

"Карточка" товара с возможностью оплатить:
http://127.0.0.1:8000/item/<pk>/

(Для тестовой успешной операции покупки введите номер карты: 4242 4242 4242 4242)

#### Технологии:
asgiref
certifi
charset-normalizer
Django
idna
python-dotenv
requests
sqlparse
stripe
tzdata
urllib3

#### Backend developer

[Владмир Максимов](https://github.com/MaksimovVS) [@MaksimovVS](https://t.me/MaksimovVS)
