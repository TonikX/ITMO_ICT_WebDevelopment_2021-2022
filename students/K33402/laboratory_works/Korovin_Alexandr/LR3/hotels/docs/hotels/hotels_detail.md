# Детально каждый отель

Удаление, обновление и получений каждого отеля по pk

**URL** : `/hotels/<int:pk>`

**Method** : `GET, PUT, DELETE`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json

[
  {
    "id": 1,
    "title": "Park Central Hotel New York",
    "img": "https://cdn.ostrovok.ru/t/640x400/content/89/56/8956ecfe1fcde9b1bf44399fad98fb7bd060f1e9.jpeg",
    "price": "от 15 066 руб.",
    "rate": 4,
    "address": "870 7th Ave, Нью-Йорк"
  }
]
  
```