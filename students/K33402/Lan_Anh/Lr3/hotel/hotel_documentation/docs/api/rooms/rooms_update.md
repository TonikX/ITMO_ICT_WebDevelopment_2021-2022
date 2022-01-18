# update Single room API

This API is meant to perform update single operation with rooms.

**URL** : `/api/rooms/:id/update`

**Method** : `PUT`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
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
}
```



