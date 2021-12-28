# Retrieve hotel total available rooms Info API

This API is meant to perform retrieve operation with hotels total available rooms.

**URL** : `/api/hotels/:id/rooms/available`

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
    ...
]
```



