# Updating and deleting chicken

Get, update and delete information about a chicken using its ID

**URL** : `/chickens/info/<int:pk>/`

**Methods** : `GET` & `PUT` & `PATCH` & `DELETE`


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "breed": "big chicken",
    "cage": "12",
    "weight": 5,
    "age": 1,
    "egg_amount": 5
}
```