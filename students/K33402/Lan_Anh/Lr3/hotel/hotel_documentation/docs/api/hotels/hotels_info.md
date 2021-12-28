# Retrieve Single hotel Info API

This API is meant to perform retrieve single operation with hotels info.

**URL** : `/api/hotels/:id/info`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Hotel": {
        "id": 1,
        "owner": {
            "username": "host_tranthanh",
            "first_name": "Tran Thanh",
            "last_name": "Huynh",
            "email": "tranthanhhuynh@gmail.com",
            "phone": "32152123",
            "sex": "M",
            "license": "II",
            "workExp": 2
        },
        "name": "Marina Bay Sand",
        "address": "singapore",
        "description": "marina bay sand is a good hotel"
    },
    "Info": {
        "total_rooms": 3,
        "available_rooms": 2,
        "min_price": 20,
        "max_price": 80,
        "average_price": 50
    }
}
```



