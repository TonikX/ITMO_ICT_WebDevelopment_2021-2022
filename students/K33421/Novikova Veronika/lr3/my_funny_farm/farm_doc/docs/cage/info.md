# Updating and deleting cage

Get, update and delete information about a cage using its ID

**URL** : `/cage/info/<int:pk>/`

**Methods** : `GET` & `PUT` & `PATCH` & `DELETE`


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "shed": 1,
    "row": 9,
    "cage": 12,
    "square": 10
}
```