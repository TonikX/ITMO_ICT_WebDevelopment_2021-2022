# Вход

**URL** : `/auth/jwt/create/`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data constraints** :
```json
{
  "username": "string",
  "password": "string"
}
```

## Success Responses

**Code** : `200 ОК`

**Content** : 

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDE2OTE4OSwianRpIjoiMjI2ZDU5MzYwMzFjNDM3Y2E4YjFlNzk4M2M0NmZkYWUiLCJ1c2VyX2lkIjoxfQ.zNXjIdvCYSAYbHRn_HjfeBSa-wWk6m7Lrwtt2cGbz9Y",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MTY5MTg5LCJqdGkiOiI4ZWY3NzA1MGViZTQ0YzlhOTUwNWI3ZTI5YmQ2ZTEzOCIsInVzZXJfaWQiOjF9.63RVhaF5MBUwSwknVIyJRlsBSfugGZqNLrrII88hcig"
}
```