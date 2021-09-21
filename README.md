# Инструкция по запуску проекта

---
## Инструкция для запуска docker-compose

1. Склонировать репозиторий на хостовую машину
2. Создать в директории `./movies_admin` файл `.env` вручную или посредством команды `touch ./movies_admin/.env`
3. Заполнить файл `.env` следующими параметрами (пример лежит в `./env.dist`):
    - **SECRET_KEY** - секретный ключ приложения Django
    - **DB_ENGINE** - используемая база данных
    - **DB_NAME** - имя подключаемой базы данных
    - **DB_USER** - имя пользователя базы данных
    - **DB_PASSWORD** - пароль пользователя базы данных
    - **DB_HOST** - хост базы данных (для текущей сборки - `database`)
    - **DB_PORT** - порт для подключения к базе данных (по умолчанию - `5432`)
    - **ALLOWED_HOSTS** - ALLOWED_HOSTS приложения Django
4. Выполнить последовательно следующие команты:
    - `docker compose build`
    - `docker compose up -d`
5. **В случае, если сборка запускается впервые, нужно выполнить следующие действия:**
    - Необходимо подключиться к контейнеру Django с помощью команды ``docker exec -it movies_admin bash``
    - Создать суперпользователя ``python manage.py createsuperuser``
    - Отключиться от контейнера: `exit`
6. Открыть [созданную панель администратора](http://0.0.0.0/admin) и авторизоваться

___

# Техническое задание

В качестве второго задания предлагаем расширить проект «Панель администратора»: запустить приложение через WSGI/ASGI,
настроить отдачу статических файлов через Nginx и подготовить инфраструктуру для работы с Docker. Для этого перенесите в
репозиторий код, который вы написали в первом спринте, и выполните задания из папки `tasks`.

## Используемые технологии

- Приложение запускается под управлением сервера WSGI/ASGI.
- Для отдачи [статических файлов](https://nginx.org/ru/docs/beginners_guide.html#static) используется **Nginx.**
- Виртуализация осуществляется в **Docker.**

## Основные компоненты системы

1. **Cервер WSGI/ASGI** — сервер с запущенным приложением.
2. **Nginx** — прокси-сервер, который является точкой входа для web-приложения.
3. **PostgreSQL** — реляционное хранилище данных.
4. **ETL** — механизм обновления данных между PostgreSQL и ES.

## Схема сервиса

![all](images/all.png)

## Требования к проекту

1. Приложение должно быть запущено через WSGI/ASGI.
2. Все компоненты системы находятся в Docker.
3. Отдача статических файлов осуществляется за счёт Nginx.

## Рекомендации к проекту

1. Для работы с WSGI/ASGI-сервером база данных использует специального юзера.
2. Для взаимодействия между контейнерами используйте docker compose.
