# Эндпоинты


* ##Получить список всех услуг </br>
**URL** : `/api/service/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Services": [
    {
        "id": 1,
        "title": "Продвижение в FB",
        "price": 2000
    }
]
}
```


* ##Обновить заявку </br>


**URL** : `api/application/<int:pk>/update`

**Method** : `PUT`/`PATCH`

**Data constraints** : `{}`

**Content-Type** : application/json

**Пример запроса**
```json
{
    "id": 2,
    "phone": "7936329798",
    "email": "magazinschiki@yandex.ru",
    "price": 2000,
    "quantity": 1,
    "client": 2,
    "worker": 1,
    "service": 5
}
```

**Результат**
HTTP 200 OK
Allow: PUT, PATCH, OPTIONS
Content-Type: application/json
Vary: Accept


* ##Обновить данные об услуге </br>


**URL** : `api/service/<int:pk>/update`

**Method** : `PUT`/`PATCH`

**Data constraints** : `{}`

**Content-Type** : application/json

**Пример запроса**
```json
{
    "title": "Продвижение VK",
    "price": 4000
}
```

**Результат**
HTTP 200 OK
Allow: PUT, PATCH, OPTIONS
Content-Type: application/json
Vary: Accept