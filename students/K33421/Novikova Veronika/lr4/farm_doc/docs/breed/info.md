# Updating and deleting breed

Get, update and delete information about a breed using its ID

**URL** : `/breeds/info/<int:pk>/`

**Methods** : `GET` & `PUT` & `PATCH` & `DELETE`


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "breed": "small chicken",
    "avg_eggs": 3,
    "avg_weight": 2,
    "diet": "table 5"
}
```