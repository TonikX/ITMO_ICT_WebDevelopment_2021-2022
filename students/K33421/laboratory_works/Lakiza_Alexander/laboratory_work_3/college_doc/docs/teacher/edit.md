### Изменить/удалить данные о преподавателе 

**URL** : `/teacher/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 2,
    "subjects": [
        {
            "name": "Русский язык"
        }
    ],
    "first_name": "Валентина",
    "last_name": "Шерстнева",
    "room": "26"
}
```