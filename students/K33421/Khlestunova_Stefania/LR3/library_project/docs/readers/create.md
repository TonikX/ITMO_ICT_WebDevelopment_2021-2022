# Create Reader

Создает объект-читатель в таблице читатели.

**URL** : `/library/readers/create/`

**Allow** : `POST, OPTIONS`

**HTTP 201 CREATED**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 3,
    "reader_ticket_number": 102939,
    "first_name": "Frank",
    "last_name": "Коневский",
    "passport": "1230229384",
    "birth_date": "2001-01-02",
    "address": "Какой-то адрес",
    "phone_number": "89124832213",
    "education": "h",
    "scientist": "0",
    "attached_books": [],
    "hall": []
}
```