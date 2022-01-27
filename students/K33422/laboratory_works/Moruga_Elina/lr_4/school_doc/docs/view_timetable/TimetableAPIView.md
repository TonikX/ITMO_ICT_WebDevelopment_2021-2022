# TimetableAPIView

## Показать расписание

**URL** : `/timetable/`

**Allow** : GET, HEAD, OPTIONS

## Success Responses

**Code** : `200 OK`

**Content-Type** : application/json

**Vary** : Accept

```json
{
    [
        {
            "id": 3,
            "day_of_week": "1",
            "lesson": "2",
            "teacher_id": 8,
            "room_id": 4,
            "subject_id": 9,
            "class_id": 7
        },
        {
            "id": 4,
            "day_of_week": "1",
            "lesson": "3",
            "teacher_id": 8,
            "room_id": 3,
            "subject_id": 10,
            "class_id": 6
        }
    ]
}
```