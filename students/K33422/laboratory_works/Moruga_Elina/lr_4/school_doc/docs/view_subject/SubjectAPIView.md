# SubjectAPIView

## Показать все предметы

**URL** : `/subjects/`

**Allow** : GET, HEAD, OPTIONS

## Success Responses

**Code** : `200 OK`

**Content-Type** : application/json

**Vary** : Accept

```json
{
    [
        {
            "id": 5,
            "subject": "Русский язык",
            "status": "basic",
            "teacher_id": 7
        },
        {
            "id": 6,
            "subject": "Литература",
            "status": "basic",
            "teacher_id": 7
        }
    ]
}
```