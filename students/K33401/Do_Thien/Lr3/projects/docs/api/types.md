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
   "Types": [
       {
        "id": 1,
        "name": "1",
        "price": 300
    },
    {
        "id": 2,
        "name": "2",
        "price": 650
    },
    {
        "id": 3,
        "name": "3",
        "price": 1000
    }
   ]
}
```