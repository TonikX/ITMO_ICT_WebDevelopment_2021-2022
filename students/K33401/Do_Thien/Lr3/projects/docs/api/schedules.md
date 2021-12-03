# Показать всех воинов

Get all information about guest.

**URL** : `/api/guests/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Schedules": [
       {
        "id": 1,
        "staff_id": {
            "id": 1,
            "first_name": "Tanjiro",
            "last_name": "Kamado",
            "middle_name": "",
            "date_of_birth": "2000-12-09",
            "phone": "8291291",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "date": "2021-11-01"
    },
    {
        "id": 2,
        "staff_id": {
            "id": 2,
            "first_name": "Nezuko",
            "last_name": "Kamado",
            "middle_name": "",
            "date_of_birth": "1999-12-01",
            "phone": "8291292132",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "date": "2021-11-01"
    },
    {
        "id": 3,
        "staff_id": {
            "id": 3,
            "first_name": "Zenitsu",
            "last_name": "Agatsuma",
            "middle_name": "",
            "date_of_birth": "2000-12-18",
            "phone": "891241924",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "date": "2021-11-01"
    },
    {
        "id": 4,
        "staff_id": {
            "id": 4,
            "first_name": "Inosuke",
            "last_name": "Hashibira",
            "middle_name": "",
            "date_of_birth": "2000-08-20",
            "phone": "8141947129",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "date": "2021-11-15"
    },
    {
        "id": 5,
        "staff_id": {
            "id": 1,
            "first_name": "Tanjiro",
            "last_name": "Kamado",
            "middle_name": "",
            "date_of_birth": "2000-12-09",
            "phone": "8291291",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "date": "2021-11-15"
    },
    {
        "id": 6,
        "staff_id": {
            "id": 2,
            "first_name": "Nezuko",
            "last_name": "Kamado",
            "middle_name": "",
            "date_of_birth": "1999-12-01",
            "phone": "8291292132",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "date": "2021-11-15"
    },
    {
        "id": 7,
        "staff_id": {
            "id": 3,
            "first_name": "Zenitsu",
            "last_name": "Agatsuma",
            "middle_name": "",
            "date_of_birth": "2000-12-18",
            "phone": "891241924",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 1,
            "number": 1
        },
        "date": "2021-12-01"
    },
    {
        "id": 8,
        "staff_id": {
            "id": 4,
            "first_name": "Inosuke",
            "last_name": "Hashibira",
            "middle_name": "",
            "date_of_birth": "2000-08-20",
            "phone": "8141947129",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 2,
            "number": 2
        },
        "date": "2021-12-01"
    },
    {
        "id": 9,
        "staff_id": {
            "id": 1,
            "first_name": "Tanjiro",
            "last_name": "Kamado",
            "middle_name": "",
            "date_of_birth": "2000-12-09",
            "phone": "8291291",
            "address": "vp 57"
        },
        "floor_id": {
            "id": 3,
            "number": 3
        },
        "date": "2021-11-01"
    }
   ]
}
```