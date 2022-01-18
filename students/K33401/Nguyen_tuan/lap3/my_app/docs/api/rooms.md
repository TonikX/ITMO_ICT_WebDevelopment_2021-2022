# Показать всех

**URL** : `/api/warriors/`

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
            "name": "single",
            "price": 400
        },
        "status_id": {
            "id": 1,
            "name": "full"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "name": 181,
        "phone": "12345"
    },
    {
        "id": 2,
        "type_id": {
            "id": 1,
            "name": "single",
            "price": 400
        },
        "status_id": {
            "id": 2,
            "name": "empty"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "name": 182,
        "phone": "12346"
    },
    {
        "id": 3,
        "type_id": {
            "id": 2,
            "name": "double",
            "price": 600
        },
        "status_id": {
            "id": 1,
            "name": "full"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "name": 271,
        "phone": "123434"
    },
    {
        "id": 4,
        "type_id": {
            "id": 2,
            "name": "double",
            "price": 600
        },
        "status_id": {
            "id": 2,
            "name": "empty"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "name": 231,
        "phone": "12841273"
    },
    {
        "id": 5,
        "type_id": {
            "id": 3,
            "name": "tripble",
            "price": 800
        },
        "status_id": {
            "id": 1,
            "name": "full"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "name": 310,
        "phone": "1247124-"
    },
    {
        "id": 6,
        "type_id": {
            "id": 3,
            "name": "tripble",
            "price": 800
        },
        "status_id": {
            "id": 2,
            "name": "empty"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "name": 341,
        "phone": "19241274"
    }
   ]
}
```