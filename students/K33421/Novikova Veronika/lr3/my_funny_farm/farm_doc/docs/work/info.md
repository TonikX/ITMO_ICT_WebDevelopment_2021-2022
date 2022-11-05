# Updating and deleting task

Get, update and delete information about a task using its ID

**URL** : `/work/info/<int:pk>/`

**Methods** : `GET` & `PUT` & `PATCH` & `DELETE`


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 5,
    "work": "clean",
    "username": 4,
    "cage": 2
}
```