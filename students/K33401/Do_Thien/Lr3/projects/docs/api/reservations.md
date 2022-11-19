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
    {
        "id": 2,
        "room_id": {
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
        "guest_id": {
            "id": 2,
            "first_name": "Mitsuri",
            "last_name": "Kanroji",
            "middle_name": "",
            "date_of_birth": "2000-12-30",
            "address": "5/7 vp",
            "city": "Moscow",
            "email": "",
            "phone": "89211111111",
            "passport": "C1111111"
        },
        "date": "2021-10-04",
        "check_in": "2021-10-04",
        "check_out": "2021-10-12",
        "adults": 2,
        "children": 0,
        "amount": 5000
    },
    {
        "id": 3,
        "room_id": {
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
        "guest_id": {
            "id": 3,
            "first_name": "Obana",
            "last_name": "Iguro",
            "middle_name": "",
            "date_of_birth": "2000-12-08",
            "address": "VP 5/7",
            "city": "Kazan",
            "email": "",
            "phone": "897777777",
            "passport": "C5555555"
        },
        "date": "2021-11-01",
        "check_in": "2021-11-01",
        "check_out": "2021-11-10",
        "adults": 3,
        "children": 1,
        "amount": 10000
    },
    {
        "id": 4,
        "room_id": {
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
        "guest_id": {
            "id": 4,
            "first_name": "Sanemi",
            "last_name": "Shinazugawa",
            "middle_name": "",
            "date_of_birth": "2000-08-12",
            "address": "VP 5/7",
            "city": "Saint Petersburg",
            "email": "",
            "phone": "897777777",
            "passport": "C5555555"
        },
        "date": "2021-12-01",
        "check_in": "2021-12-01",
        "check_out": "2021-12-10",
        "adults": 1,
        "children": 0,
        "amount": 3000
    }
   ]
}
```