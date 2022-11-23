# Создание отелей с many=true

Создание отелей

**URL** : `/hotels/create`

**Method** : `POST`

**Auth required** : NO

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
  },
  {
    "id": 2,
    "title": "New York Hilton Midtown",
    "img": "https://cdn.ostrovok.ru/t/640x400/content/9f/04/9f042c9badf624961bac812df79fa24d6be93969.jpeg",
    "price": "от 20 311 руб.",
    "rate": 4,
    "address": "1335 6th Ave, Нью-Йорк"
  },
  {
    "id": 3,
    "title": "ОтельPennsylvania",
    "img": "https://cdn.ostrovok.ru/t/640x400/content/9f/97/9f97d818722c52a50812cd9d71047ebc9d2d5543.jpeg",
    "price": "от 14 041 руб.",
    "rate": 2,
    "address": "401 Seventh Avenue , Нью-Йорк"
  },
  {
    "id": 4,
    "title": "Waldorf Astoria",
    "img": "https://cdn.ostrovok.ru/t/640x400/content/6f/7d/6f7d0653694de8975a30d2932f09102f3c1dc972.jpeg",
    "price": "от 21 841 руб.",
    "rate": 5,
    "address": "301 Park Avenue, Нью-Йорк"
  }
]
```