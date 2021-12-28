# list Single host API

This API is meant to perform list operation with hosts.

**URL** : `/api/hosts/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "host_tranthanh",
        "first_name": "Tran Thanh",
        "last_name": "Huynh",
        "email": "tranthanhhuynh@gmail.com",
        "phone": "32152123",
        "sex": "M",
        "license": "II",
        "workExp": 2
    },
    {
        "username": "host_luuhuonggiang",
        "first_name": "Huong Giang",
        "last_name": "Luu",
        "email": "luuhuonggiang@gmail.com",
        "phone": "3215222",
        "sex": "F",
        "license": "III",
        "workExp": 4
    }
]
```