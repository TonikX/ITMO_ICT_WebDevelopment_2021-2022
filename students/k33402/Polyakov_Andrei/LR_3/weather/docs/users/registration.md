# Регистрация пользователя

Use this endpoint to add new user.

**URL** : `/auth/users/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201`

**Content** : `{}`

```json
{
  "email": "user@example.com",
  "username": "string",
  "id": 0,
  "password": "string"
}
```