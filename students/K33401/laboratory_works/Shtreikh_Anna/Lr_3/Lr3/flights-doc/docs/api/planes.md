## PLANE endpoints

### List of airplanes

**URL** : `planes/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
     {
        "id": 1,
        "company": "YYY lines",
        "model": "Airbus320",
        "prod_date": "2022-02-24"
    },
    {
        "id": 2,
        "company": "YYY lines",
        "model": "Airbus380",
        "prod_date": "2022-01-24"
    },
    {
        "id": 3,
        "company": "YourWave",
        "model": "Boeing 737-500",
        "prod_date": "2010-02-24"
    },
    {
        "id": 4,
        "company": "YourWave",
        "model": "Boeing 767",
        "prod_date": "2012-02-24"
    }
```

### Add a new plane

**URL** : `planes/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
     "company": null,
     "model": "",
     "prod_date": "null"
}
```

### Modify (get/update/delete) an existing plane

**URL** : `planes/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "company": "YourWave",
    "model": "Boeing 767",
    "prod_date": "2012-02-24"
}
```