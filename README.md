# Web-приложение для заполнения форм.

## 1. Зависимости
Для запуска проекта потребуется:
- Docker Desktop

## 2. Установка
```shell script
# Запуск контейнера
docker compose up -d

# Остановка контейнера
docker compose down
```

## 3. Использование
> Все дальнейшие действия должны производится при запущенном контейнере.

### Вариант - 1
- Вы можете протестировать работу приложения с помощью`Postman` или `Insomnia`.

### Вариант - 2
- Вы можете протестировать работу приложения с помощью `DRF`.
- Чтобы получить список всех данных из БД отправь GET запрос по адресу:

```
http://127.0.0.1:8000/get_form
```

### Вариант - 3
- Вы можете протестировать работу приложения набрав в адресной строке:

```
http://127.0.0.1:8000/form/get_form/
```