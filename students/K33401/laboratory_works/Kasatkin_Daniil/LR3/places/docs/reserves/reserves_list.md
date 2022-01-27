Выводит информацию информацию обо всех бронях

**URL** : `/reserves/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```json
[
  {
    "id": 1,
    "guest": {
      "id": 1,
      "password": "pbkdf2_sha256$320000$WqfGI7IC1P4MhfWFYwx4RV$c1JFPxsv3mzJe7RBcSDVBLX4b2jOSkuECL3vmXLZUwc=",
      "last_login": "2022-01-04T10:05:13.434077Z",
      "is_superuser": true,
      "phone_number": "+79630983774",
      "email": "a@a.com",
      "first_name": "admin",
      "join_date": "2022-01-04T10:05:02.629885Z",
      "is_staff": true,
      "is_host": true,
      "is_active": true,
      "groups": [],
      "user_permissions": []
    },
    "place": {
      "id": 4,
      "host": {
        "id": 1,
        "password": "pbkdf2_sha256$320000$WqfGI7IC1P4MhfWFYwx4RV$c1JFPxsv3mzJe7RBcSDVBLX4b2jOSkuECL3vmXLZUwc=",
        "last_login": "2022-01-04T10:05:13.434077Z",
        "is_superuser": true,
        "phone_number": "+79630983774",
        "email": "a@a.com",
        "first_name": "admin",
        "join_date": "2022-01-04T10:05:02.629885Z",
        "is_staff": true,
        "is_host": true,
        "is_active": true,
        "groups": [],
        "user_permissions": []
      },
      "place_type": "House",
      "place_offers": "Wifi, Kitchen, Free parking on premises, Shampoo, Hot water, Body soap, Body Washer, Bed linens, Smoke alarm, Cooking basics, TV, Air conditioning, Hair dryer",
      "title": "YOUR winter home in St Petersburg,FL",
      "desc": "The perfect winter getaway. This home in St Petersburg, is close to 275, with a short trip to the beaches, downtown and shopping.\nAll you need to do is pack your toothbrush and a few clothes, then ENJOY.",
      "beds": 3,
      "bedrooms": 2,
      "bathrooms": 2,
      "guests": 4,
      "location": "Florida, United States",
      "image": "http://127.0.0.1:8000/images/places/YOUR%20winter%20home%20in%20St%20Petersburg%2CFL/d772d338-6ac3-4ed7-9cc5-43706fd7181e.webp",
      "price": 5360
    },
    "check_in_date": "2022-01-09",
    "check_out_date": "2022-01-12",
    "guests_count": 2
  },
  {
    "id": 2,
    "guest": {
      "id": 1,
      "password": "pbkdf2_sha256$320000$WqfGI7IC1P4MhfWFYwx4RV$c1JFPxsv3mzJe7RBcSDVBLX4b2jOSkuECL3vmXLZUwc=",
      "last_login": "2022-01-04T10:05:13.434077Z",
      "is_superuser": true,
      "phone_number": "+79630983774",
      "email": "a@a.com",
      "first_name": "admin",
      "join_date": "2022-01-04T10:05:02.629885Z",
      "is_staff": true,
      "is_host": true,
      "is_active": true,
      "groups": [],
      "user_permissions": []
    },
    "place": {
      "id": 4,
      "host": {
        "id": 1,
        "password": "pbkdf2_sha256$320000$WqfGI7IC1P4MhfWFYwx4RV$c1JFPxsv3mzJe7RBcSDVBLX4b2jOSkuECL3vmXLZUwc=",
        "last_login": "2022-01-04T10:05:13.434077Z",
        "is_superuser": true,
        "phone_number": "+79630983774",
        "email": "a@a.com",
        "first_name": "admin",
        "join_date": "2022-01-04T10:05:02.629885Z",
        "is_staff": true,
        "is_host": true,
        "is_active": true,
        "groups": [],
        "user_permissions": []
      },
      "place_type": "House",
      "place_offers": "Wifi, Kitchen, Free parking on premises, Shampoo, Hot water, Body soap, Body Washer, Bed linens, Smoke alarm, Cooking basics, TV, Air conditioning, Hair dryer",
      "title": "YOUR winter home in St Petersburg,FL",
      "desc": "The perfect winter getaway. This home in St Petersburg, is close to 275, with a short trip to the beaches, downtown and shopping.\nAll you need to do is pack your toothbrush and a few clothes, then ENJOY.",
      "beds": 3,
      "bedrooms": 2,
      "bathrooms": 2,
      "guests": 4,
      "location": "Florida, United States",
      "image": "http://127.0.0.1:8000/images/places/YOUR%20winter%20home%20in%20St%20Petersburg%2CFL/d772d338-6ac3-4ed7-9cc5-43706fd7181e.webp",
      "price": 5360
    },
    "check_in_date": "2022-01-15",
    "check_out_date": "2022-01-16",
    "guests_count": 2
  }
]
```