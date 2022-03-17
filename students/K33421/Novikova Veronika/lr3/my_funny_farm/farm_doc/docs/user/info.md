# Updating and deleting user

Get, update and delete information about a user using its ID

**URL** : `/users/info/<int:pk>/`

**Methods** : `GET` & `PUT` & `PATCH` & `DELETE`

**Auth required** : `YES`


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "username": "nika1",
    "first_name": "Veronika",
    "last_name": "Novikova",
    "passport": "123445",
    "salary": 20000,
    "cage": [
        1,
        2
    ]
}
```