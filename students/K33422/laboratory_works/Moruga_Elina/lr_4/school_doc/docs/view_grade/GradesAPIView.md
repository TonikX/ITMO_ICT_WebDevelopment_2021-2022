# GradesAPIView

## Показать все оценки

**URL** : `/grades/list/`

**Allow** : GET, HEAD, OPTIONS

## Success Responses

**Code** : `200 OK`

**Content-Type** : application/json

**Vary** : Accept

```json
{
    "Grades": [
        {
            "id": 10,
            "grade": "4",
            "quarter": "1",
            "student_id": 2,
            "subject_id": 5
        },
        {
            "id": 11,
            "grade": "5",
            "quarter": "1",
            "student_id": 2,
            "subject_id": 6
        }
    ]
}
```