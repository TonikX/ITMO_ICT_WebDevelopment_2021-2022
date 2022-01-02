# Вывод всех отзывов

Список всех отзывов

**URL** : `/reviews/`

**Method** : `GET`

**Auth required** : NO
**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{{}}`

```json

[
  {
    "id": 1,
    "author": {
      "id": 12,
      "password": "pbkdf2_sha256$260000$CMWR5WcKFkGcKrwat6Oz1W$UafE/LBQP9GsoiNVCCA+R/ZnGqf/n3rcHKpDKyoBNFY=",
      "last_login": null,
      "is_superuser": false,
      "username": "Joe",
      "first_name": "",
      "last_name": "",
      "email": "joe@mail.ru",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-12-21T18:10:42.036153Z",
      "groups": [],
      "user_permissions": []
    },
    "create_time": "2021-12-22T17:53:22.655567Z",
    "comment": "Amazing hotel",
    "hotel": 1
  },
  {
    "id": 2,
    "author": {
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
    "create_time": "2021-12-22T17:55:39.241478Z",
    "comment": "32321321321321321",
    "hotel": 15
  }
]

```