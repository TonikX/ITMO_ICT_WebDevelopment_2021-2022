# Create Single Booking API

This API is meant to perform create operation with bookings.

**URL** : `/api/bookings/create`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "booking_code": "A501",
    "date_checkin": "2021-12-26",
    "date_checkout": "2021-12-28",
    "main_guest": 2,
    "room": 1
}
```



