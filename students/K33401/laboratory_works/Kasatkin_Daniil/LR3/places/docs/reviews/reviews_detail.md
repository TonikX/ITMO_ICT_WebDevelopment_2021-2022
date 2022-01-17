Выводит информацию информацию, удаляет или изменяет отзыв по pk

**URL** : `/reviews/<int:pk>`

**Method** : `GET, PUT, PATCH, DELETE`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
    "id": 1,
    "desc": "1212",
    "review_date": "2022-01-10",
    "value": 1,
    "author": 1,
    "place": 4
}
```