# Показать всех воинов и их профессии

Выводит информацию обо всех воинах и их профессиях

**URL** : `/warriors_professions/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Warriors and their professions": [
    {
        "id": 1,
        "profession": {
            "title": "Cool",
            "description": "The best"
        },
        "race": "s",
        "name": "Ivan",
        "level": 2,
        "skill": []
    }
]
}
```