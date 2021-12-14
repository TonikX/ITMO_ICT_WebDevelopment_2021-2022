# UPDATE

Update schedule by ID

**URL** : `/api/schedule/<id>/update/`

**Method** : `PATCH`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
       {
           "id": 1,
           "date_register": "2021-10-10",
           "date_checkin": "2021-10-10",
           "date_checkout": "2021-10-15",
           "time_checkin": "15:00:00",
           "time_checkout": "12:00:00"
       }
]
```

