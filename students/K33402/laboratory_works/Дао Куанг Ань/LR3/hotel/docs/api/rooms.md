# Show all rooms

Get infos about all rooms

**URL** : `/api/room/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
       {
           "id": 1,
           "number": "101",
           "type": "Double",
           "price": 1000,
           "state": "+",
           "floor": 1
       },
       {
           "id": 2,
           "number": "201",
           "type": "Single",
           "price": 1000,
           "state": "-",
           "floor": 2
       }
]
```

