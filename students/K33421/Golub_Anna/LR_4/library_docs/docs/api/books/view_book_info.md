# View book info

**URL** : `books/<int:pk>/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "book_hall": [
        {
            "id": 1,
            "number": 1,
            "title": "Русская классика",
            "capacity": 10
        }
    ],
    "book_reader": [],
    "title": "Война и мир",
    "authors": "Л. Толстой",
    "publisher": "Русская классика",
    "publication_year": 1888,
    "genre": "Роман",
    "book_cypher": "111"
}
```

