# Показать всех воинов

Get all information about room.

**URL** : `/api/rooms/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Rooms": [
       {
        "id": 1,
        "type_id": {
            "id": 1,
            "name": "1",
            "price": 300
        },
        "status_id": {
            "id": 1,
            "name": "e"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "number": "101",
        "phone": "8101"
    },
    {
        "id": 2,
        "type_id": {
            "id": 2,
            "name": "2",
            "price": 650
        },
        "status_id": {
            "id": 2,
            "name": "f"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "number": "102",
        "phone": "8102"
    },
    {
        "id": 3,
        "type_id": {
            "id": 3,
            "name": "3",
            "price": 1000
        },
        "status_id": {
            "id": 1,
            "name": "e"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "number": "103",
        "phone": "8103"
    },
    {
        "id": 4,
        "type_id": {
            "id": 1,
            "name": "1",
            "price": 300
        },
        "status_id": {
            "id": 1,
            "name": "e"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "number": "201",
        "phone": "8201"
    },
    {
        "id": 5,
        "type_id": {
            "id": 2,
            "name": "2",
            "price": 650
        },
        "status_id": {
            "id": 2,
            "name": "f"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "number": "202",
        "phone": "8202"
    },
    {
        "id": 6,
        "type_id": {
            "id": 2,
            "name": "2",
            "price": 650
        },
        "status_id": {
            "id": 1,
            "name": "e"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "number": "203",
        "phone": "8203"
    },
    {
        "id": 7,
        "type_id": {
            "id": 1,
            "name": "1",
            "price": 300
        },
        "status_id": {
            "id": 1,
            "name": "e"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "number": "301",
        "phone": "8301"
    },
    {
        "id": 8,
        "type_id": {
            "id": 2,
            "name": "2",
            "price": 650
        },
        "status_id": {
            "id": 2,
            "name": "f"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "number": "302",
        "phone": "8302"
    },
    {
        "id": 9,
        "type_id": {
            "id": 3,
            "name": "3",
            "price": 1000
        },
        "status_id": {
            "id": 1,
            "name": "e"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "number": "303",
        "phone": "8303"
    }
   ]
}
```