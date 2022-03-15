# Reader's books w names

Показывает расширенную информацию об опр. пользователе и названия взятых им книг

**URL** : `/library/readers/<int:pk>/books/`

**Allow** : `GET, HEAD, OPTIONS'

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 2,
    "attached_books": [
        "451 градус по Фаренгейту",
        "Константин"
    ],
    "reader_ticket_number": 123983,
    "first_name": "Ronda",
    "last_name": "Kadara",
    "passport": "1234120983",
    "birth_date": "2021-07-21",
    "address": "Какой-то адрес",
    "phone_number": "10928384743",
    "education": "h",
    "scientist": "1",
    "hall": [
        2
    ]
}
```