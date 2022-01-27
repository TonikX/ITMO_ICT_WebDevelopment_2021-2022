# RoomAPIView

## Показать все кабинеты

**URL** : `rooms/`

**Allow** : GET, HEAD, OPTIONS

## Success Responses

**Code** : `200 OK`

**Content-Type** : application/json

**Vary** : Accept

```json
{
    [
        {
            "id": 1,
            "room": 1
        },
        {
            "id": 2,
            "room": 2
        }
    ]
}
```