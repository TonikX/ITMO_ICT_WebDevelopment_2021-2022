# list Single Booking API

This API is meant to perform list operation with bookings.

**URL** : `/api/bookings/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Bookings":[
        {
            "id": 1,
            "booking_code": "A501",
            "date_checkin": "2021-12-26",
            "date_checkout": "2021-12-28",
            "main_guest": 2,
            "room": 1
        },
        {
            "id": 2,
            "booking_code": "F530",
            "date_checkin": "2021-11-26",
            "date_checkout": "2021-12-03",
            "main_guest": 1,
            "room": 2
        },
        ...
    ]
}
```