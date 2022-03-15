# List of readers

Выводит список зарегестрированных читателей.

**URL** : `/library/readers/list/`

**Allow** : `GET, HEAD, OPTIONS`

**Params** : `age_l (старше), age_g (младше), instances_lte (экземпляров книг меньше), instances_gte (экземпляров книг больше), to_date (взяли книги до даты), from_date (взяли книги после даты)`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "Readers":[
        {
            "id": 1,
            "reader_ticket_number": 123982,
            "first_name": "Dara",
            "last_name": "Kadara",
            "passport": "1234578964",
            "birth_date": "2021-07-22",
            "address": "Карамбе, Аляска",
            "phone_number": "89124832213",
            "education": "m",
            "scientist": "0",
            "attached_books": [
                1
            ],
            "hall": [
               1
            ]
        },
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
    ]
}
```