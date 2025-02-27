# skymarket
```sh
Это сайт с объявлениями поддерживающий поиск по названию товаров и авторизацию пользователей.
```

<img src="home_page.png" alt="site" style="height: 420;" />

## Установка:
```sh
● Установить переменные окружения в .env.sample и переименовать его в .env
● В файле .env BASE_URL указываем localhost если вы разворачиваете локально либо айпи удалённого сервера соответственно для корректной работы фронта
● Если будете размещать на удалённом сервере, надо будет править пути на фронте в файлах AuthContext.js:22, axiosInstance.js:5, MainContext.js:20,172, useAxios.js:7 localhost заменить на ваш хост
```

## Docker-compose:
```sh
● Склонировать репозиторий
● Установить docker и docker-compose командой apt install docker.io docker-compose
● Сбилдить и запустить в корне проекта командами docker-compose build docker-compose up
● После этого заходим на http://ваш_хост:3000 либо на документацию к backend http://ваш_хост:8001/api/swagger
```

## Только бэкенд:
```sh
● Убедитесь, что у вас установлен python 3.11 или более новая версия
● Убедитесь, что у вас установлен PostgreSQL и запущен локальный сервер базы данных
● Склонировать репозиторий и перейти в корень проекта
● Создать и активировать виртуальное окружениеpython -m venv venv
● Активировать source venv/bin/activate
● Установить зависимости командой pip install -r requirements.txt
● Создать вашу базу данных для работы с проектом CREATE DATABASE ваша_база_данных;
● Применить миграции python3 manage.py migrate
● Загрузить фикстуры для тестов командой python3 manage.py loadall
● Открыть командную строку и запустить python3 manage.py runserver 
```

## Используемые технологии
```sh
● Frontend на React
● DjangoRestFramework
● Djoser для CRUD-модели пользователя
● Simple_jwt для токенов
● Документация по эндпоинтам /api/swagger/, работает авторизация по Bearer токену
● CORS
● Пагинация объявлений(требования фронтенда), права доступа, роль модератора и пользователя и др.
```

## Эндпоинты:
```sh
● Регистрация пользователя
● Просмотр деталей профиля
● Редактирование профиля
● Удаление пользователя
● Получение токена
● Обновление токена
● Список объявлений с пагинацией
● Список своих объявлений с пагинацией
● Создание объявления
● Редактирование объявления
● Удаление объявления
● Список комментариев к объявлению
● Создание комментария к объявлению
● Редактирование комментария к объявлению
● Удаление комментария к объявлению
```

## Права доступа:
```sh
● Анонимный пользователь видит только список объявлений
● Пользователь может:
  ○ Получать список объявлений
  ○ Получать одно объявление
  ○ Создавать объявление
  ○ Редактировать и удалять своё объявление(реализовано только в бэкенде)
  ○ Получать список комментариев к объявлению
  ○ Создавать комментарии к объявлению
  ○ Редактировать/удалять комментарии к объявлению(реализовано только в бэкенде)
● Администратор может:
  ○ Дополнительно к правам пользователя редактировать или удалять объявления и комментарии к объявлениям любых других пользователей(реализовано только в бэкенде)
```

### Цель проекта
```sh
Код написан в образовательных целях.
```
