# list Single visitor API

This API is meant to perform list operation with visitors.

**URL** : `/api/visitors/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "guest_lananh",
        "first_name": "Lan Anh",
        "last_name": "Le",
        "email": "guest_lananhnobi@gmail.com",
        "phone": "3215215",
        "sex": "F",
        "nationality": "Vietnam",
        "passport_no": "C3212521"
    },
    {
        "username": "guest_quangvan",
        "first_name": "Quang Van",
        "last_name": "Tran",
        "email": "lusanney@gmail.com",
        "phone": "0401993309",
        "sex": "M",
        "nationality": "Vietnam",
        "passport_no": "C3212a234"
    }
]
```