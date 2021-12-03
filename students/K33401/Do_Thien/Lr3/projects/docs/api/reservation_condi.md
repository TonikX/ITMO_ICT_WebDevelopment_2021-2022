# Показать всех воинов

Get all information about guest.

**URL** : `/api/guests/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[http://127.0.0.1:8000/reservations/all/?room=101&check_in=2021-10-01&check_out=2021-10-03]}`

```json
{
   "Reservations": [
       {
        "id": 1,
        "room_id": {
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
        "guest_id": {
            "id": 1,
            "first_name": "Giyu",
            "last_name": "Tomioka",
            "middle_name": "",
            "date_of_birth": "2000-12-18",
            "address": "VP 5/7",
            "city": "Saint Petersburg",
            "email": "",
            "phone": "89876543210",
            "passport": "C9999999"
        },
        "date": "2021-10-01",
        "check_in": "2021-10-01",
        "check_out": "2021-10-05",
        "adults": 1,
        "children": 0,
        "amount": 1500
    },  
   ]
}
```