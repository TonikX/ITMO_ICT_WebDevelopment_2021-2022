# Показать всех воинов

Выводит информацию обо всех войнах

**URL** : `/warriors/list/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Warriors": [
    {
        "id": 1,
        "race": "s",
        "name": "Ivan",
        "level": 2,
        "profession": 1,
        "skill": []
    }
]
}
```