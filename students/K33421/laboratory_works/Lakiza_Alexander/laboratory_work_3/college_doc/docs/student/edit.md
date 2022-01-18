### Изменить/удалить данные о студенте 

**URL** : `/student/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "group": [
        {
            "id": 1,
            "name": "A100"
        }
    ],
    "first_name": "Кирилл",
    "last_name": "Чернышев"
}
```