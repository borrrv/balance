Сервис для работы с балансом пользователей
## Описание
Сервис для работы с балансом пользователей (зачисление средств, списание средств, перевод средств от пользователя к пользователю, а также метод получения баланса пользователя).
## Технологии
- Django 3.2
- DRF 3.14
- Djoser 2.1
- PostgreSQL 15
## Запуск проекта
- Клонировать репозиторий к себе на компьютер
- Создать и активировать виртуальное окружение
```
python -m venv env
source env/scripts/activate
python3 -m pip install --upgrade pip
```
- Установить зависимости
```
pip install -r requirements.txt
```
- Создать в директории с файлом ```manage.py``` файл .env
- Добавить в него следующие переменные(переменные предназначены для PostgreSQL):
```
DEBUG
ALLOWED_HOSTS
DB_ENGINE
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
```
- Применить миграции
```
python manage.py migrate
```
- Запустить проект
```
Python manage.py runserver
```
## Примеры запросов
Посмотреть документацию по доступным запросам можно при запущенном проекте по ссылке: http://127.0.0.1:8000/redoc/

Для того, чтобы не запутаться в работе пользователя, ниже приведены примеры основных запросов
- (POST) Создание нового пользователя
```
api/users/
```
- (POST) Получение токена для работы пользователя
```
api/auth/token/login/
```
- (GET) Просмотр информации о текущем пользователе
```
api/users/me/
```
- (PATCH) Пополнение баланса текущего пользователя
```
api/money/2/
```
- (POST) Добавление услуги в заказ
```
/api/service/1/add/
```
- (POST) Резервирование средств на отдельном счете
```
api/users/reserve/
```
- (POST) Признание выручки выбранного пользователя по ```id```(доступно только администратору)
```
api/users/2/revenue/
```
- (PATCH) Перевод средств другому пользователю
```
api/users/2/transaction/
```
## Планируется сделать
- Настроить workflow.
- Использовать docker и docker-compose для поднятия и развертывания dev-среды.
### Автор
[Vladislav](https://github.com/borrrv)
