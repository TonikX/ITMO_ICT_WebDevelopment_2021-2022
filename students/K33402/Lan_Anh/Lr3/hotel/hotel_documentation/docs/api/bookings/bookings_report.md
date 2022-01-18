# Retrieve Single Booking Report API

This API is meant to perform retrieve single operation with booking report.

**URL** : `/api/bookings/:id/report`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Booking": {
        "id": 1,
        "bills": [
            {
                "id": 1,
                "service_name": "Stay",
                "description": "stay cost",
                "total": 160,
                "booking": 1
            }
        ],
        "main_guest": {
            "username": "guest_lananh",
            "first_name": "Lan Anh",
            "last_name": "Le",
            "email": "guest_lananhnobi@gmail.com",
            "phone": "3215215",
            "sex": "F",
            "nationality": "Vietnam",
            "passport_no": "C3212521"
        },
        "room": {
            "id": 1,
            "hotel": {
                "id": 1,
                "name": "Marina Bay Sand",
                "address": "singapore",
                "description": "marina bay sand is a good hotel",
                "owner": 4
            },
            "number": 302,
            "price": 50,
            "state": "AV"
        },
        "booking_code": "A501",
        "date_checkin": "2021-12-26",
        "date_checkout": "2021-12-28"
    },
    "Report": {
        "total_price": 160,
        "total_days": 2
    }
}
```



