# HotelManager
### Get started

```python manage.py runserver```

```mkdocs serve```

## Available endpoints

###Authentication request
* `/auth/token/login/` - Авторизация
#####Пример POST:
```
{
    "password": "root",
    "username": "root"
}
```
#####Результат:

```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "auth_token": "41asdhu12h3jsadkh37721y38ashdjwadu23h4kjashd"
}
```

* `/auth/token/logout/` - Выход
#####Пример POST:
```
{}
```
#####Результат:
```
HTTP 204 No Content
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept
```

* `/auth/users` - Регистрация
#####Пример POST:
```
{
    "email": "example@gmail.com",
    "username": "example",
    "password": "exampleexample"
}
```
#####Результат:
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "example@gmail.com",
    "username": "example",
    "id": 9
}
```

###Get request
* `/hotel/guests/{pk}` - Получить информацию о конкретном госте
* `/hotel/rooms/{pk}` - Получить информацию о конкретной комнате
* `/hotel/staff/{pk}` - Получить информацию о конкретном члене персонала
* `/hotel/cleaning/{pk}` - Получить информацию о конкретной уборке
* `/hotel/cleaning` - Получить информацию о всех уборках
* `/hotel/guests` - Получить информацию о всех гостях
* `/hotel/rooms` - Получить информацию о всех комнатах
* `/hotel/staff` - Получить информацию о всех членах персонала



###Post request
* `/hotel/rooms` - Добавить номер
* `/hotel/guests` - Добавить гостя
* `/hotel/staff` - Добавить члена персонала
* `/hotel/cleaning` - Добавить уборку

###Put/Patch request
* `/hotel/guests/{pk}` - Изменить информацию о конкретном госте
* `/hotel/rooms/{pk}` - Изменить информацию о конкретной комнате
* `/hotel/staff/{pk}` - Изменить информацию о конкретном члене персонала
* `/hotel/cleaning/{pk}` - Изменить информацию о конкретной уборке


###Delete request
* `/hotel/guests/{pk}` - Удалить информацию о конкретном госте
* `/hotel/rooms/{pk}` - Удалить информацию о конкретной комнате
* `/hotel/staff/{pk}` - Удалить информацию о конкретном члене персонала
* `/hotel/cleaning/{pk}` - Удалить информацию о конкретной уборке