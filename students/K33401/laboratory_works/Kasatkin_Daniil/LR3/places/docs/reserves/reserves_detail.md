Выводит информацию информацию, удаляет или изменяет бронь по pk

**URL** : `/reserves/<int:pk>`

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
  "check_in_date": "2022-01-09",
  "check_out_date": "2022-01-12",
  "guests_count": 2,
  "guest": 1,
  "place": 4
}
```