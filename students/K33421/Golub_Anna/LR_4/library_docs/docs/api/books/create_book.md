# Create a new book

**URL** : `books/create/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201 Created`

**Content** : `{[]}`

```json
{
    "id": 3,
    "title": "Евгений Онегин",
    "authors": "А. Пушкин",
    "publisher": "Русская классика",
    "publication_year": 1957,
    "genre": "Поэма",
    "book_cypher": "444",
    "book_hall": [],
    "book_reader": []
}
```