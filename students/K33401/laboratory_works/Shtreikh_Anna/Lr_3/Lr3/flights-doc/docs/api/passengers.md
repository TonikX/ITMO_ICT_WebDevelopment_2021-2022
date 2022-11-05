## Passengers endpoints

### List of passengers

**URL** : `passengers/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "first_name": "Anna",
        "last_name": "Shtreikh"
    },
    {
        "first_name": "Maria",
        "last_name": "Gold"
    },
    {
        "first_name": "Rem",
        "last_name": "King"
    },
    {
        "first_name": "Jo",
        "last_name": "Noy"
    },
    {
        "first_name": "Kamila",
        "last_name": "Valieva"
    },
    {
        "first_name": "Lili",
        "last_name": "Ur"
    }
```

### Add a new plane

**URL** : `passengers/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "first_name": "",
    "last_name": "",
    "username": "",
    "password": ""
}
```

### Modify (get/update/delete) an existing plane

**URL** : `passengers/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "first_name": "Kamila",
    "last_name": "Valieva",
    "username": "Kamila",
    "password": "qwe"
}
```