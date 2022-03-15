# Показать всех воинов, их профессии и умения

Выводит информацию обо всех воинах, их профессиях и умениях

**URL** : `/warriors_skills/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Warriors, their professions and skills": [
    {
        "id": 1,
        "skill": [
            "Strength",
            "Agility"
        ],
        "race": "s",
        "name": "Ivan",
        "level": 2,
        "profession": 1
    }
]
}
```