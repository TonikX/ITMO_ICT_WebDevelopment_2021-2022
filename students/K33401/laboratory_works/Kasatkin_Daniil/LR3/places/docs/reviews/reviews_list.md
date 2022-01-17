Выводит информацию информацию обо всех отзывах

**URL** : `/reviews/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```json
[
  {
    "id": 1,
    "author": {
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
    "desc": "1212",
    "review_date": "2022-01-10",
    "value": 1
  },
  {
    "id": 2,
    "author": {
      "id": 3,
      "password": "pbkdf2_sha256$320000$KEc4nxqUPOaFhe07zDqqg7$dMNl07LZtwXA1iP2646Yn/CSA+6w76XyFz9v0eqMa70=",
      "last_login": null,
      "is_superuser": false,
      "phone_number": "+79630983773",
      "email": "b@b.com",
      "first_name": "Artem",
      "join_date": "2022-01-07T12:01:34.829051Z",
      "is_staff": false,
      "is_host": true,
      "is_active": true,
      "groups": [],
      "user_permissions": []
    },
    "place": {
      "id": 5,
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
      "place_offers": "Kitchen, Free parking on premises, Air conditioning, Shampoo, Body Washer, Bed linens",
      "title": "Casa Del Prince Upper",
      "desc": "Come enjoy the unique Shabby chic sleeping and sitting area furnishings in French design motif. Reminiscent of New Orleans; all in new construction Studio apartments. Brilliant Brass decorative touch's; will remind you of Louie Armstrong's trumpet! Apartments feature all the comforts of home, including your own in-unit washer and dryer. Located in the quiet, convenient and historic Euclid St. Paul / Crescent Lake neighborhood of St. Petersburg.",
      "beds": 1,
      "bedrooms": 1,
      "bathrooms": 1,
      "guests": 2,
      "location": "Saint Petersburg",
      "image": "http://127.0.0.1:8000/images/places/Casa%20Del%20Prince%20Upper/2.webp",
      "price": 8782
    },
    "desc": "asdadas",
    "review_date": "2022-01-10",
    "value": 3
  }
]
```