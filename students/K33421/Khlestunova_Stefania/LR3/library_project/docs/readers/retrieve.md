# Retrieve Reader

Показывает расширенную информацию об опр. читателе.

**URL** : `/library/readers/<int:pk>/`

**Allow** : `GET, HEAD, OPTIONS'

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 2,
    "reader_ticket_number": 123983,
    "first_name": "Ronda",
    "last_name": "Kadara",
    "passport": "1234120983",
    "birth_date": "2021-07-21",
    "address": "Какой-то адрес",
    "phone_number": "10928384743",
    "education": "h",
    "scientist": "1",
    "attached_books": [
        3,
        2
    ],
    "hall": [
        2
    ]
},
```