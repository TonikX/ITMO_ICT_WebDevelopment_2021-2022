# Edit or delete a ReaderBook instance

**URL** : `/return/<int:pk>/`

**Method** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 5,
    "issue_date": "2020-02-23",
    "due_date": "2020-02-23",
    "book": 3,
    "reader": 12
}
```