# List Halls

Выводит список всех залов.

**URL** : `/library/halls/list/`

**Allow** : `GET, HEAD, OPTIONS`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
[
    {
        "id": 1,
        "hall_num": 2,
        "hall_name": "МегаКнига",
        "capacity": 200
    },
    {
        "id": 2,
        "hall_num": 1,
        "hall_name": "МиниКнига",
        "capacity": 100
    },
    {
        "id": 3,
        "hall_num": 3,
        "hall_name": "МакроКниги",
        "capacity": 500
    }
]
```
