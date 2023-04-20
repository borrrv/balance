# Сервис для работы с балансом пользователей
## Описание
Сервис для работы с балансом пользователей (зачисление средств, списание средств, перевод средств от пользователя к пользователю, а также метод получения баланса пользователя).

Проект поднимается в 3 контейнерах: web, nginx, postgres

Написан скрипт, который во время сборки контейнера ```postgres``` создает новую таблицу ```balance``` с пользователем ```balance_user```, имеющим все привилегии для этой таблицы.

Также настроен workflow, который при пуше в гит проверяет проект по pep8.
## Технологии
- Python 3.8
- Django 3.2
- DRF 3.14
- Djoser 2.1
- PostgreSQL 15
## Запуск проекта(Linux, WSL2)
- Клонировать репозиторий к себе на компьютер
```
git clone https://github.com/borrrv/balance.git
```
- Установить Docker и Docker-compose.
```
sudo apt install docker-ce docker-compose -y
```
- Перейти в папку ```balance``` с файлом ```docker-compose.yaml``` и ввести команду
```
sudo docker-compose up -d --build
```
- В терминале выполнить следующие команды
```
sudo docker-compose exec web python manage.py makemigrations
sudo docker-compose exec web python manage.py migrate
```
- Услуги можно добавить только через админку, чтобы это сделать выполните следующие действия:

В терминале ввести команды.
```
sudo docker-compose exec web python manage.py collectstatic
sudo docker-compose exec web python manage.py createsuperuser(создать суперпользователя)
```
- Перейти по ссылке: http://localhost/admin/, войти под суперпользователем, создать несколько услуг.

#### Теперь проект готов к работе

## Примеры запросов*
Посмотреть документацию по доступным запросам можно при запущенном проекте по ссылке: http://localhost/redoc/

Для того, чтобы не запутаться в работе пользователя(у эндпоинта ```users``` много функционала из-за djoser), ниже приведены примеры основных запросов.

*-все запросы выполнять относительно http://localhost/
- (POST) Создание нового пользователя
```
/api/users/
```
- (POST) Получение токена для работы пользователя
```
/api/auth/token/login/
```
- (GET) Просмотр информации о текущем пользователе
```
/api/users/me/
```
- (PATCH) Пополнение баланса текущего пользователя
```
/api/money/2/
```
- (POST) Добавление услуги в заказ
```
/api/service/1/add/
```
- (POST) Резервирование средств на отдельном счете
```
/api/users/reserve/
```
- (POST) Признание выручки выбранного пользователя по ```id```(доступно только администратору)
```
/api/users/2/revenue/
```
- (PATCH) Перевод средств другому пользователю
```
/api/users/2/transaction/
```

### Автор
[Vladislav](https://github.com/borrrv)
