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
   "Guests": [
       {
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
    {
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
    {
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
    {
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
    {
        "id": 5,
        "first_name": "Gyomei",
        "last_name": "Himejima",
        "middle_name": "",
        "date_of_birth": "2000-08-12",
        "address": "VP 5/7",
        "city": "Saint Petersburg",
        "email": "",
        "phone": "897777777",
        "passport": "C88888"
    },
    {
        "id": 6,
        "first_name": "Tengen",
        "last_name": "Uzui",
        "middle_name": "",
        "date_of_birth": "2000-08-12",
        "address": "VP 5/7",
        "city": "Saint Petersburg",
        "email": "",
        "phone": "897777777",
        "passport": "C88888"
    },
    {
        "id": 7,
        "first_name": "Muichiro",
        "last_name": "Tokito",
        "middle_name": "",
        "date_of_birth": "2000-08-12",
        "address": "VP 5/7",
        "city": "Moscow",
        "email": "",
        "phone": "897777777",
        "passport": "C88888"
    },
    {
        "id": 8,
        "first_name": "Shinobu",
        "last_name": "Kocho",
        "middle_name": "",
        "date_of_birth": "2000-08-12",
        "address": "VP 5/7",
        "city": "Moscow",
        "email": "",
        "phone": "897777777",
        "passport": "C88888"
    },
    {
        "id": 9,
        "first_name": "Kanae",
        "last_name": "Kocho",
        "middle_name": "",
        "date_of_birth": "2000-08-12",
        "address": "VP 5/7",
        "city": "Ha Noi",
        "email": "",
        "phone": "897777777",
        "passport": "C88888"
    },
    {
        "id": 10,
        "first_name": "Kyojuro",
        "last_name": "Rengoku",
        "middle_name": "",
        "date_of_birth": "2000-08-12",
        "address": "VP 5/7",
        "city": "Kazan",
        "email": "",
        "phone": "897777777",
        "passport": "C88888"
    }
   ]
}
```