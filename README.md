```bash
python -m venv venv
```
Активировать виртуальное окружение
```bash
venv/Scripts/activate
```
Установить зависимости проекта из файла `requirements.txt`
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py add_payment
```
```bash
python3 manage.py csu
```
Запустить сервер
```bash
python manage.py runserver
```
Необходимо создать файл .env.docker и заполнить параметры
```bash
    POSTGRES_DB=/имя вашей базы данных/
    POSTGRES_USER='app'
    POSTGRES_PASSWORD=/ваш пароль от базы данных/
    POSTGRES_HOST='db'
    POSTGRES_PORT=/ваш host(стандартный 5432)/
```
Запустить docker
```bash
 docker-compose up -d --build
```