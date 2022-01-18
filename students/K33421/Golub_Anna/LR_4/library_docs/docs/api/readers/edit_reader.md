# Edit a reader info or delete a reader

**URL** : `readers/edit/<int:pk>/`

**Method** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 2,
    "last_login": null,
    "is_superuser": false,
    "email": "",
    "is_staff": false,
    "is_active": false,
    "date_joined": "2021-12-08T11:50:26.300755Z",
    "username": "alina",
    "password": "11r11",
    "card_number": 1,
    "first_name": "Alina",
    "last_name": "Ivanova",
    "passport": "1111111111",
    "date_of_birth": "2000-10-10",
    "address": "г. Санкт-Петербург",
    "phone": "89111111111",
    "education": "Высшее",
    "degree": false,
    "reader_hall": 1,
    "groups": [],
    "user_permissions": [
        20
    ],
    "reader_book": []
}
```