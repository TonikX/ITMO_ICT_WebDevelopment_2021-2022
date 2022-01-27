# StudentAPIView

## Показать всех учеников

**URL** : `/students/list/`

**Allow** : GET, HEAD, OPTIONS

## Success Responses

**Code** : `200 OK`

**Content-Type** : application/json

**Vary** : Accept

```json
{
    [
        {
            "id": 2,
            "first_name": "Sergey",
            "last_name": "Morozov",
            "gender": "male"
        },
        {
            "id": 3,
            "first_name": "Petr",
            "last_name": "Sobakin",
            "gender": "male"
        }
    ]
}
```