# Информация о пользователе

Use this endpoint to obtain user information.

**URL** : `/auth/users/me/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200`

**Content** : `{}`

```json
{
    "email": "user@example.com",
    "id": 0,
    "username": "string"
}
```