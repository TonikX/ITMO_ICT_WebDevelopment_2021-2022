# Регистрация

**URL** : `/auth/users/`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data constraints** :
```json
{
  "email": "user@example.com",
  "username": "string",
  "password": "string"
}
```

## Success Responses

**Code** : `201 Created`

**Content** : 

```json
{
  "email": "user@example.com",
  "username": "string",
  "id": 0
}
```