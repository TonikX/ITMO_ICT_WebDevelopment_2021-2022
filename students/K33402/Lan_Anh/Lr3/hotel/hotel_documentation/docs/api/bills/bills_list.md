# list Single bill API

This API is meant to perform list operation with bills.

**URL** : `/api/bills/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "service_name": "Stay",
        "description": "stay cost",
        "total": 160,
        "booking": 1
    }
]
```