# BookAttachments List

Выводит список записей о заимствовании книг пользователями.

**URL** : `/library/book_attachment/list/`

**Allow** : `GET, HEAD, OPTION`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
[
    {
        "id": 1,
        "attach_date": "2022-01-17T20:10:52Z",
        "book": 1,
        "reader": 1
    },
    {
        "id": 2,
        "attach_date": "2022-01-17T20:10:59Z",
        "book": 3,
        "reader": 2
    },
    {
        "id": 3,
        "attach_date": "2022-01-17T20:11:08Z",
        "book": 2,
        "reader": 2
    },
    {
        "id": 4,
        "attach_date": "2022-01-22T21:23:00Z",
        "book": 4,
        "reader": 3
    }
]
```