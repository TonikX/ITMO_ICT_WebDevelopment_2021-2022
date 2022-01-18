# Edit a book info or delete a book

**URL** : `books/edit/<int:pk>/`

**Method** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

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
}
```


## Readers
* `readers/` - list all readers
* `readers/create/` - create a new reader
* `readers/<int:pk>/` - view reader info
* `readers/edit/<int:pk>/` - update reader info or delete a reader