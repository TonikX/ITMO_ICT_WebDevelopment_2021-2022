# Купить билет

**URL** : `/tickets/bookings`

**Method** : `POST`

**Auth required** : Yes

**Permissions required** : None

**Data constraints** : 
```json
{
  "flight": "integer"
}
```

## Success Responses

**Code** : `201 Created`

**Content** : 

```json
{
  "id": 2,
  "flight": 2
}
```