-Открыть терминал
-Перейти в дерикторию %%%/test_project  (дериктория в которой содержится файл manage.py)

Прописать следующие команды:

(для Linux используйте pip3 и python3)

-pip install -r requirements.txt

-python makemigrations

-python manage.py migrate

-python manage.py runserver (запуск сервера)


'http://127.0.0.1:8000/admin/' -чтобы зайти в админ-панель после запуска сервера нужно перейти по адресу  (Имя пользователя - admin , Пароль - admin) 

'http://127.0.0.1:8000/v.1/'   -выведет конечные точки, по которым можно перейти и получить соответствующую информацию
