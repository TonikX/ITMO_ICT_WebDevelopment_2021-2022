# Получение токена пользователя

Use this endpoint to obtain user authentication token.

**URL** : `/auth/token/login/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201`

**Content** : `{}`

```json
{
    "auth_token": "string"
}
```