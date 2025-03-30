## Company endpoints

### List of companies

**URL** : `tickets/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "id": 1,
        "flight": {
            "id": 1,
            "number": "689GY7",
            "departure": "2022-03-24T14:46:08Z",
            "arrival": "2022-03-24T16:46:12Z",
            "wherefrom": "Moskow",
            "whereto": "Berlin",
            "gate": "10",
            "plane": 1
        },
        "passenger": {
            "first_name": "Maria",
            "last_name": "Gold"
        },
        "number": "678Hy"
    },
    {
        "id": 2,
        "flight": {
            "id": 2,
            "number": "666HHt7",
            "departure": "2022-03-25T14:47:07Z",
            "arrival": "2022-02-26T00:47:13Z",
            "wherefrom": "Moskow",
            "whereto": "Mexico",
            "gate": "8",
            "plane": 2
        },
        "passenger": {
            "first_name": "Jo",
            "last_name": "Noy"
        },
        "number": "7779ngg"
    },
    {
        "id": 3,
        "flight": {
            "id": 3,
            "number": "99I8y9",
            "departure": "2022-03-14T14:47:50Z",
            "arrival": "2022-03-14T16:48:14Z",
            "wherefrom": "Moskow",
            "whereto": "Berlin",
            "gate": "7",
            "plane": 3
        },
        "passenger": {
            "first_name": "Rem",
            "last_name": "King"
        },
        "number": "99I8y9999"
    },
    {
        "id": 4,
        "flight": {
            "id": 4,
            "number": "77Ia45",
            "departure": "2022-02-28T14:48:37Z",
            "arrival": "2022-02-28T16:48:14Z",
            "wherefrom": "Moskow",
            "whereto": "Berlin",
            "gate": "6",
            "plane": 4
        },
        "passenger": {
            "first_name": "Anna",
            "last_name": "Shtreikh"
        },
        "number": "555Tyu"
    }
```

### Add a new plane

**URL** : `tickets/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": "",
    "flight": null,
    "passenger": null
}
```

### Modify (get/update/delete) an existing plane

**URL** : `tickets/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": "879Fhk7",
    "flight": "HYK76L, Moskow -> Berlin",
    "passenger": "Mary - Maria Gold"
}
```