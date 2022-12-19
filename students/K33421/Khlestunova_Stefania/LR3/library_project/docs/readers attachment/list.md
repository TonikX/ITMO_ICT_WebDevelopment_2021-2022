# ReadersAttachments List

Выводит список записей о регистрации читателей в зале.

**URL** : `/library/readers_attachment/list/`

**Allow** : `GET, HEAD, OPTION`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
[
    {
        "id": 1,
        "attach_date": "2022-01-15T21:04:25Z",
        "reader": 1,
        "hall": 1
    },
    {
        "id": 2,
        "attach_date": "2022-01-17T16:24:23Z",
        "reader": 2,
        "hall": 2
    },
    {
        "id": 3,
        "attach_date": "2022-02-21T21:23:00Z",
        "reader": 2,
        "hall": 2
    }
]
```