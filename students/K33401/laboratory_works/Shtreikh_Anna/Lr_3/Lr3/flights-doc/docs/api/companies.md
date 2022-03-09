## Company endpoints

### List of companies

**URL** : `airlines/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
      {
        "id": 1,
        "name": "YYY lines",
        "owner": "Mark Holl",
        "phone": "8988666553"
    },
    {
        "id": 2,
        "name": "YourWave",
        "owner": "Mary Giogri",
        "phone": "6988656553"
    }
```

### Add a new plane

**URL** : `airlines/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "",
    "owner": "",
    "phone": ""
}
```

### Modify (get/update/delete) an existing plane

**URL** : `airlines/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "YourWave",
    "owner": "Mary Giogri",
    "phone": "6988656553"
}
```