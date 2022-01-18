# List all books

**URL** : `/books/`

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
        "title": "Война и мир",
        "authors": "Л. Толстой",
        "publisher": "Русская классика",
        "publication_year": 1888,
        "genre": "Роман",
        "book_cypher": "111",
        "book_hall": [
            1
        ],
        "book_reader": []
    },
    {
        "id": 2,
        "title": "Янки при дворе короля Артура",
        "authors": "Марк Твен",
        "publisher": "Зарубежная классика",
        "publication_year": 1910,
        "genre": "Приключенческий роман",
        "book_cypher": "222",
        "book_hall": [
            2
        ],
        "book_reader": []
    }
```

