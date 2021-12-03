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
   "Staffs": [
       {
        "id": 1,
        "first_name": "Tanjiro",
        "last_name": "Kamado",
        "middle_name": "",
        "date_of_birth": "2000-12-09",
        "phone": "8291291",
        "address": "vp 57"
    },
    {
        "id": 2,
        "first_name": "Nezuko",
        "last_name": "Kamado",
        "middle_name": "",
        "date_of_birth": "1999-12-01",
        "phone": "8291292132",
        "address": "vp 57"
    },
    {
        "id": 3,
        "first_name": "Zenitsu",
        "last_name": "Agatsuma",
        "middle_name": "",
        "date_of_birth": "2000-12-18",
        "phone": "891241924",
        "address": "vp 57"
    },
    {
        "id": 4,
        "first_name": "Inosuke",
        "last_name": "Hashibira",
        "middle_name": "",
        "date_of_birth": "2000-08-20",
        "phone": "8141947129",
        "address": "vp 57"
    }
   ]
}
```