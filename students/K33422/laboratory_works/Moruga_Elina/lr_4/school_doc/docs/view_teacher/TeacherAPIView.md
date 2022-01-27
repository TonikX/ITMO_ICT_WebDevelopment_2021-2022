# TeacherAPIView

## Показать всех учителей

**URL** : `/teachers/list/`

**Allow** : GET, HEAD, OPTIONS

## Success Responses

**Code** : `200 OK`

**Content-Type** : application/json

**Vary** : Accept

```json
{
    [
        {
            "username": "teacher_1",
            "first_name": "Elena",
            "last_name": "Cherepahova",
            "patronymic": "Sergeevna",
            "email": "teacher1@mail.ru"
        },
        {
            "username": "teacher_2",
            "first_name": "Sergey",
            "last_name": "Slonov",
            "patronymic": "Petrovich",
            "email": "teacher2@mail.ru"
        }
    ]
}
```
