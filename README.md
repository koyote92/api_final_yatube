# yatube_api
Данный проект представляет из себя API для проекта Yatube.
Реализованы все возможности, доступные в web-версии приложения:
- создание/редактирование/удаление публикаций
- комментирование публикаций
- оформление подписки на других авторов

## Установка
1. Необходимо клонировать репозиторий на свой компьютер при помощи команды:
```
git@github.com:koyote92/api_final_yatube.git
```
2. Перейти в папку с проектом:
```
cd api_final_yatube
```
3. Создать виртуальное окружение:
```
python3 -m venv venv
```
4. Активировать созданное виртуальное окружение:
* Для Linux/macOS:
```
source venv/bin/activate
```
* Для Windows
```
source venv/Scripts/activate
```
5. Установить необходимые зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
6. Перейти в базовую папку и выполнить миграции:
```
cd yatube_api
```
```
python manage.py migrate
```
7. Запустить проект:
```
python manage.py runserver
```

## Работа с Yatube API
Для запросов к API необходим токен, который можно получить по url-адресу:
```
POST http://your-domain.com/api/v1/jwt/create/

{
  "username": "string",
  "password": "string"
}
```
### Примеры запросов #
Получение списка публикаций:
```
GET http://your-domain.com/api/v1/posts/
```
Создание собственной публикации:
```
POST http://your-domain.com/api/v1/posts/

{
  "text": "string",
  "image": "string",
  "group": 0
}
```
### Подробная документация по запросам к API доступна по адресу:
```
http://your-domain.com/redoc/
```
## Стэк технологий:
- Django
- Django REST Framework
- Simple JSON Web Token

## Авторы
Приложение posts, основные настройки проекта, документация:
```
https://github.com/evi1ghost
```
```
https://github.com/a-ershov
```
```
https://github.com/TurboKach
```
```
https://github.com/yandex-praktikum
```
Приложение API:
```
https://github.com/koyote92
```
Ревьюер проекта:
- Алексей Григорьев