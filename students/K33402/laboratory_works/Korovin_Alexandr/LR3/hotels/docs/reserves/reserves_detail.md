# Детально каждая бронь

Удаление, обновление и получений каждой брони по pk

**URL** : `/reserves/<int:pk>`

**Method** : `GET, PUT, DELETE`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json


{
  "id": 14,
  "guest": {
    "id": 8,
    "password": "pbkdf2_sha256$260000$5eqFdQe29KfWqKS8PeaTWm$oTyfVC0MlbG/nTXOVG1D74VXRUAnL31LNcpmmkcVP/o=",
    "last_login": null,
    "is_superuser": false,
    "username": "Test1",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2021-12-21T17:42:08.444467Z",
    "groups": [],
    "user_permissions": []
  },
  "hotel": {
    "id": 26,
    "title": "Holiday Inn Express Hotel&Suites NEARSEAWORLD,an IHGHotel",
    "img": "https://cdn.ostrovok.ru/t/640x400/content/fa/zz/faad3876445c52ef439e5907edf2290f4e300767.jpeg",
    "price": "от 9460 руб.",
    "rate": 2,
    "address": "9536 Amelia Pass, Сан-Антонио"
  },
  "create_time": "2021-12-22T16:51:44.475285Z",
  "check_in_date": "2021-12-22",
  "check_out_date": "2021-12-23",
  "guests_count": 5
}


```