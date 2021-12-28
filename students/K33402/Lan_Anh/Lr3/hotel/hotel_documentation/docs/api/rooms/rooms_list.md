# list Single room API

This API is meant to perform list operation with rooms.

**URL** : `/api/rooms/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "hotel": {
            "id": 1,
            "name": "Marina Bay Sand",
            "address": "singapore",
            "description": "marina bay sand is a good hotel",
            "owner": 4
        },
        "number": 302,
        "price": 50,
        "state": "AV"
    },
    {
        "id": 2,
        "hotel": {
            "id": 2,
            "name": "Marriot",
            "address": "Ha noi vietnam",
            "description": "marriot is the old hotel",
            "owner": 5
        },
        "number": 311,
        "price": 30,
        "state": "AV"
    },
    ...
]
```