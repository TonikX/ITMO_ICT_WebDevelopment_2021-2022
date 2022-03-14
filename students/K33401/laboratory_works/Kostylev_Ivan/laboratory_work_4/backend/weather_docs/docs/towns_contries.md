# Work with towns and contries

# Towns

## Get all towns

**URL** : `/town/all/`

**Method** : `GET`

**Auth required** : YES

**Request body (example)** : empty

### Success Response

**Code** : `200 OK`

```json
{
    "towns": [
        {
            "id": 1,
            "name": "Perm",
            "lon": 56.316666,
            "lat": 58.0,
            "country": 1
        },
        {
            "id": 2,
            "name": "Moscow",
            "lon": 37.618423,
            "lat": 55.751244,
            "country": 1
        },
        {
            "id": 3,
            "name": "Saint Petersburg",
            "lon": 30.308611,
            "lat": 59.9375,
            "country": 1
        }
    ]
}
```

### Failure

Check your token

**Code** : `401 Unauthorized`

## Create new town

Create new town by longitude, latitude and country

**URL** : `/town/create`

**Method** : `POST`

**Auth required** : YES

**Request body (example)** : 
```json
{
    "name": "Berlin",
    "lon": 13.404954,
    "lat": 52.520008,
    "country": 2
}
```

### Success Response

Response with id.

**Code** : `200 OK`

```json
{
    "id": 4,
    "name": "Berlin",
    "lon": 13.404954,
    "lat": 52.520008,
    "country": 2
}
```


# Countries
## Get all countries

**URL** : `/country/all/`

**Method** : `GET`

**Auth required** : YES

**Request body (example)** : empty

### Success Response

**Code** : `200 OK`

```json
{
    "towns": [
        {
            "id": 1,
            "name": "Russia",
            "continent": "EU"
        },
        {
            "id": 2,
            "name": "Germany",
            "continent": "EU"
        },
        {
            "id": 3,
            "name": "China",
            "continent": "AS"
        },
        {
            "id": 4,
            "name": "Russia",
            "continent": "AS"
        }
    ]
}
```

### Failure

Check your token

**Code** : `401 Unauthorized`


## Create new country

Create new country

**URL** : `/country/create/`

**Method** : `POST`

**Auth required** : YES

**Request body (example)** : 
```json
{
    "name": "France",
    "continent": "EU"
}
```

### Success Response

Response with id.

**Code** : `200 OK`

```json
{
    "id": 5,
    "name": "France",
    "continent": "EU"
}
```