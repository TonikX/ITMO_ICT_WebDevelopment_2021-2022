# Мои билеты

**URL** : `/tickets/my-bookings`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
[
  {
    "id": 1,
    "flight": {
      "id": 1,
      "company": {
        "id": 1,
        "name": "pobeda",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Logo-pobeda-en.svg/2560px-Logo-pobeda-en.svg.png"
      },
      "departure_airport": {
        "id": 1,
        "name": "St. Petersburg LED",
        "city_name": "St. Petersburg"
      },
      "arrival_airport": {
        "id": 2,
        "name": "Moscow DME",
        "city_name": "Moscow"
      },
      "departure_datetime": "2022-01-27T19:00:00+03:00",
      "arrival_datetime": "2022-01-28T00:00:00+03:00",
      "price": 4000,
      "flight_length": "5:00:00"
    }
  },
  {
    "id": 2,
    "flight": {
      "id": 2,
      "company": {
        "id": 1,
        "name": "pobeda",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Logo-pobeda-en.svg/2560px-Logo-pobeda-en.svg.png"
      },
      "departure_airport": {
        "id": 1,
        "name": "St. Petersburg LED",
        "city_name": "St. Petersburg"
      },
      "arrival_airport": {
        "id": 3,
        "name": "Vladivostok VVO",
        "city_name": "Vladivostok"
      },
      "departure_datetime": "2022-01-28T19:00:00+03:00",
      "arrival_datetime": "2022-01-29T02:00:00+03:00",
      "price": 40000,
      "flight_length": "7:00:00"
    }
  }
]
```