# Редактирование профиля

**URL** : `/profiles/my-profile`

**Method** : `PUT`

**Auth required** : Yes

**Permissions required** : None

**Data constraints** :
```json
{
  "email": "user@example.com",
  "profile_picture": "string"
}
```

## Success Responses

**Code** : `200 ОК`

**Content** : 

```json
{
  "id": 0,
  "email": "user@example.com",
  "profile_picture": "string",
  "bonus_count": 0,
  "bookings_count": "string"
}
```